use pyo3::prelude::*;

mod trade;
use trade::Trade;

mod portfolio;
use portfolio::Portfolio;

#[pymodule]
fn hawk(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    m.add_class::<Trade>()?;
    m.add_class::<Portfolio>()?;
    Ok(())
}
