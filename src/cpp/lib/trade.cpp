#include "trade.h"

namespace hawk {

Trade::Trade(const std::string& ts, const std::string& sym, const std::string& act,
             int qty, double prc)
    : timestamp(ts), symbol(sym), action(act), quantity(qty), price(prc), value(qty * prc) {
}

} // namespace hawk