"""Main backtesting engine"""

import hawk_core
import pandas as pd
from typing import Dict, Any

class BacktestEngine:
    """Simple backtesting engine for learning"""
    
    def __init__(self, initial_cash: float = 10000.0):
        hawk_core.initialize()
        self.portfolio = hawk_core.Portfolio(initial_cash)
        self.initial_cash = initial_cash
        
    def run_backtest(self, data: pd.DataFrame, strategy, symbol: str = "STOCK") -> Dict[str, Any]:
        """Run backtest with data and strategy"""
        
        print(f"🚀 Running backtest: {strategy.name}")
        print(f"💰 Initial capital: ${self.initial_cash:,.2f}")
        print(f"📊 Data points: {len(data):,}")
        
        trades_count = 0
        equity_curve = []
        
        for i in range(len(data)):
            timestamp = str(data.index[i])
            current_price = data['Close'].iloc[i]
            
            # Generate signal
            signal = strategy.generate_signal(data, i)
            
            # Execute trade
            if signal:
                success = self.portfolio.execute_trade(
                    timestamp, symbol, signal['action'], 
                    signal['quantity'], signal['price']
                )
                if success:
                    trades_count += 1
            
            # Track equity
            portfolio_value = self.portfolio.calculate_total_value({symbol: current_price})
            equity_curve.append({
                'timestamp': timestamp,
                'value': portfolio_value,
                'price': current_price
            })
        
        # Calculate results
        final_value = equity_curve[-1]['value']
        total_return = (final_value - self.initial_cash) / self.initial_cash
        
        results = {
            'initial_value': self.initial_cash,
            'final_value': final_value,
            'total_return': total_return,
            'total_return_pct': total_return * 100,
            'total_trades': trades_count,
            'trades': list(self.portfolio.get_trades()),
            'equity_curve': equity_curve,
            'final_cash': self.portfolio.get_cash(),
            'final_position': self.portfolio.get_position(symbol)
        }
        
        self._print_results(results)
        return results
    
    def _print_results(self, results):
        """Print summary results"""
        print(f"\n📈 Backtest Results")
        print("=" * 30)
        print(f"Total Return: {results['total_return_pct']:.2f}%")
        print(f"Final Value: ${results['final_value']:,.2f}")
        print(f"Total Trades: {results['total_trades']}")
        print(f"Final Cash: ${results['final_cash']:,.2f}")
        print(f"Final Position: {results['final_position']} shares")