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
    pub fn new(
        timestamp: String,
        symbol: String,
        action: String,
        quantity: i32,
        price: f64,
    ) -> Self {
        let value = f64::from(quantity) * price;
        Trade {
            timestamp,
            symbol,
            action,
            quantity,
            price,
            value,
        }
    }

    #[getter]
    pub fn timestamp(&self) -> String {
        self.timestamp.clone()
    }

    #[getter]
    pub fn symbol(&self) -> String {
        self.symbol.clone()
    }

    #[getter]
    pub fn action(&self) -> String {
        self.action.clone()
    }

    #[getter]
    pub fn quantity(&self) -> i32 {
        self.quantity
    }

    #[getter]
    pub fn price(&self) -> f64 {
        self.price
    }

    #[getter]
    pub fn value(&self) -> f64 {
        self.value
    }

    pub fn is_buy(&self) -> bool {
        self.action == "BUY"
    }

    pub fn is_sell(&self) -> bool {
        self.action == "SELL"
    }
}
