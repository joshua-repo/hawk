use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone)]
pub struct Trade {
    pub timestamp: String,
    pub symbol: String,
    pub action: String,
    pub quantity: i32,
    pub price: f64,
    pub value: f64,
}

#[pymethods]
impl Trade {
    #[new]
    pub fn new(timestamp: String, symbol: String, action: String, quantity: i32, price: f64) -> Self {
        let value = quantity as f64 * price;
        Trade {
            timestamp,
            symbol,
            action,
            quantity,
            price,
            value,
        }
    }

    pub fn is_buy(&self) -> bool {
        self.action == "BUY"
    }

    pub fn is_sell(&self) -> bool {
        self.action == "SELL"
    }
}