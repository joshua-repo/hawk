#pragma once
#include "export.h"
#include <string>

namespace hawk {

struct HAWK_API Trade {
    std::string timestamp;
    std::string symbol;
    std::string action;  // "BUY" or "SELL"
    int quantity;
    double price;
    double value;        // quantity * price
    
    Trade() = default;
    Trade(const std::string& ts, const std::string& sym, const std::string& act,
          int qty, double prc);
    
    bool is_buy() const { return action == "BUY"; }
    bool is_sell() const { return action == "SELL"; }
};

} // namespace hawk