#include "portfolio.h"
#include <stdexcept>

namespace hawk {

Portfolio::Portfolio(double initial_cash) 
    : initial_cash_(initial_cash), cash_(initial_cash) {
    if (initial_cash <= 0) {
        throw std::invalid_argument("Initial cash must be positive");
    }
}

bool Portfolio::can_buy(const std::string& symbol, int quantity, double price) const {
    if (quantity <= 0 || price <= 0) return false;
    return cash_ >= (quantity * price);
}

bool Portfolio::can_sell(const std::string& symbol, int quantity) const {
    if (quantity <= 0) return false;
    auto it = positions_.find(symbol);
    return (it != positions_.end()) && (it->second >= quantity);
}

bool Portfolio::execute_trade(const std::string& timestamp, const std::string& symbol, 
                             const std::string& action, int quantity, double price) {
    Trade trade(timestamp, symbol, action, quantity, price);
    
    if (action == "BUY" && can_buy(symbol, quantity, price)) {
        cash_ -= trade.value;
        positions_[symbol] += quantity;
        trade_history_.push_back(trade);
        return true;
    } 
    else if (action == "SELL" && can_sell(symbol, quantity)) {
        cash_ += trade.value;
        positions_[symbol] -= quantity;
        if (positions_[symbol] == 0) {
            positions_.erase(symbol);
        }
        trade_history_.push_back(trade);
        return true;
    }
    
    return false;
}

int Portfolio::get_position(const std::string& symbol) const {
    auto it = positions_.find(symbol);
    return (it != positions_.end()) ? it->second : 0;
}

double Portfolio::calculate_total_value(const std::unordered_map<std::string, double>& prices) const {
    double positions_value = 0.0;
    
    for (const auto& position : positions_) {
        auto price_it = prices.find(position.first);
        if (price_it != prices.end()) {
            positions_value += position.second * price_it->second;
        }
    }
    
    return cash_ + positions_value;
}

void Portfolio::reset() {
    cash_ = initial_cash_;
    positions_.clear();
    trade_history_.clear();
}

} // namespace hawk