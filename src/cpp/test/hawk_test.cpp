#include "portfolio.h"
#include <CLI/CLI.hpp>
#include <iostream>
#include <string>
#include <unordered_map>

int main(int argc, char** argv) {
    CLI::App app{"Hawk Portfolio CLI"};

    std::string action, timestamp, symbol;
    int quantity = 0;
    double price = 0.0;
    double initial_cash = 10000.0;

    app.add_option("--action", action, "Action (BUY/SELL)");
    app.add_option("--timestamp", timestamp, "Trade timestamp");
    app.add_option("--symbol", symbol, "Symbol");
    app.add_option("--quantity", quantity, "Quantity");
    app.add_option("--price", price, "Price");
    app.add_option("--initial-cash", initial_cash, "Initial cash")->default_val("10000.0");

    CLI11_PARSE(app, argc, argv);

    hawk::Portfolio portfolio(initial_cash);

    if (!action.empty() && !timestamp.empty() && !symbol.empty() && quantity > 0 && price > 0.0) {
        bool success = portfolio.execute_trade(timestamp, symbol, action, quantity, price);
        std::cout << (success ? "Trade executed." : "Trade failed.") << std::endl;
        std::cout << "Position: " << portfolio.get_position(symbol) << std::endl;
        std::unordered_map<std::string, double> prices = {{symbol, price}};
        std::cout << "Total value: " << portfolio.calculate_total_value(prices) << std::endl;
    } else {
        std::cout << "Missing or invalid arguments. Use --help for usage.\n";
    }

    return 0;
}