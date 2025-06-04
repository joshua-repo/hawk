#pragma once
#include "export.h"
#include "trade.h"
#include <vector>
#include <unordered_map>

namespace hawk {

class HAWK_API Portfolio {
private:
    double initial_cash_;
    double cash_;
    std::unordered_map<std::string, int> positions_;
    std::vector<Trade> trade_history_;

public:
    explicit Portfolio(double initial_cash);
    
    // Core trading functions
    bool can_buy(const std::string& symbol, int quantity, double price) const;
    bool can_sell(const std::string& symbol, int quantity) const;
    bool execute_trade(const std::string& timestamp, const std::string& symbol, 
                      const std::string& action, int quantity, double price);
    
    // Getters
    double get_cash() const { return cash_; }
    double get_initial_cash() const { return initial_cash_; }
    int get_position(const std::string& symbol) const;
    const std::vector<Trade>& get_trades() const { return trade_history_; }
    
    // Valuation
    double calculate_total_value(const std::unordered_map<std::string, double>& prices) const;
    
    // Reset
    void reset();
};

} // namespace hawk