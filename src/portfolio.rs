use crate::trade::Trade;
use pyo3::prelude::*;
use pyo3::types::PyDict;
use std::collections::HashMap;

#[pyclass]
pub struct Portfolio {
    initial_cash: f64,
    cash: f64,
    positions: HashMap<String, i32>,
    trade_history: Vec<Trade>,
}

#[pymethods]
impl Portfolio {
    #[new]
    pub fn new(initial_cash: f64) -> PyResult<Self> {
        if initial_cash <= 0.0 {
            Err(pyo3::exceptions::PyValueError::new_err(
                "Initial cash must be positive",
            ))
        } else {
            Ok(Portfolio {
                initial_cash,
                cash: initial_cash,
                positions: HashMap::new(),
                trade_history: Vec::new(),
            })
        }
    }

    pub fn can_buy(&self, _symbol: &str, quantity: i32, price: f64) -> bool {
        quantity > 0 && price > 0.0 && self.cash >= (f64::from(quantity) * price)
    }

    pub fn can_sell(&self, symbol: &str, quantity: i32) -> bool {
        quantity > 0 && self.positions.get(symbol).copied().unwrap_or(0) >= quantity
    }

    pub fn execute_trade(
        &mut self,
        timestamp: String,    // Keep String - stored in Trade
        symbol: &str,        // Change to &str - only used for lookups
        action: &str,        // Change to &str - only used for comparison
        quantity: i32,
        price: f64,
    ) -> bool {
        let trade = Trade::new(
            timestamp,
            symbol.to_string(),  // Convert to String for storage
            action.to_string(),  // Convert to String for storage
            quantity,
            price
        );
        
        if action == "BUY" && self.can_buy(symbol, quantity, price) {
            self.cash -= trade.value;
            *self.positions.entry(symbol.to_string()).or_insert(0) += quantity;
            self.trade_history.push(trade);
            true
        } else if action == "SELL" && self.can_sell(symbol, quantity) {
            self.cash += trade.value;
            if let Some(pos) = self.positions.get_mut(symbol) {
                *pos -= quantity;
                if *pos == 0 {
                    self.positions.remove(symbol);
                }
            }
            self.trade_history.push(trade);
            true
        } else {
            false
        }
    }

    pub fn get_position(&self, symbol: &str) -> i32 {
        self.positions.get(symbol).copied().unwrap_or(0)
    }

    pub fn calculate_total_value(&self, prices: &Bound<PyDict>) -> f64 {
        let mut positions_value = 0.0;
        for (symbol, qty) in &self.positions {
            if let Ok(Some(price)) = prices.get_item(symbol) {
                if let Ok(price_f64) = price.extract::<f64>() {
                    positions_value += f64::from(*qty) * price_f64;
                }
            }
        }
        self.cash + positions_value
    }

    pub fn reset(&mut self) {
        self.cash = self.initial_cash;
        self.positions.clear();
        self.trade_history.clear();
    }

    pub fn get_cash(&self) -> f64 {
        self.cash
    }

    pub fn get_initial_cash(&self) -> f64 {
        self.initial_cash
    }

    pub fn get_trades(&self) -> Vec<Trade> {
        self.trade_history.clone()
    }
}
