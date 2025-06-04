#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "core.h"

namespace py = pybind11;

PYBIND11_MODULE(hawk_core, m) {
    m.doc() = "Hawk Trading Engine - Core C++ bindings";
    
    // Trade struct
    py::class_<hawk::Trade>(m, "Trade")
        .def(py::init<const std::string&, const std::string&, const std::string&, int, double>())
        .def_readwrite("timestamp", &hawk::Trade::timestamp)
        .def_readwrite("symbol", &hawk::Trade::symbol)
        .def_readwrite("action", &hawk::Trade::action)
        .def_readwrite("quantity", &hawk::Trade::quantity)
        .def_readwrite("price", &hawk::Trade::price)
        .def_readwrite("value", &hawk::Trade::value)
        .def("is_buy", &hawk::Trade::is_buy)
        .def("is_sell", &hawk::Trade::is_sell);
    
    // Portfolio class
    py::class_<hawk::Portfolio>(m, "Portfolio")
        .def(py::init<double>())
        .def("can_buy", &hawk::Portfolio::can_buy)
        .def("can_sell", &hawk::Portfolio::can_sell)
        .def("execute_trade", &hawk::Portfolio::execute_trade)
        .def("get_cash", &hawk::Portfolio::get_cash)
        .def("get_initial_cash", &hawk::Portfolio::get_initial_cash)
        .def("get_position", &hawk::Portfolio::get_position)
        .def("get_trades", &hawk::Portfolio::get_trades, py::return_value_policy::reference_internal)
        .def("calculate_total_value", &hawk::Portfolio::calculate_total_value)
        .def("reset", &hawk::Portfolio::reset);
    
    // Module functions
    m.def("get_version", &hawk::get_version);
    m.def("initialize", &hawk::initialize);
}