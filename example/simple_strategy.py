"""Example of creating a custom strategy"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'python'))

from hawk import BacktestEngine, DataHandler
from hawk.strategy import BaseStrategy, SimpleMovingAverageStrategy

class BuyAndHoldStrategy(BaseStrategy):
    """Simple buy and hold strategy"""
    
    def __init__(self, position_size: int = 100):
        super().__init__("Buy and Hold")
        self.position_size = position_size
        self.bought = False
        
    def generate_signal(self, data, index):
        # Buy once at the beginning
        if index == 10 and not self.bought:  # Wait a few days
            self.bought = True
            return {
                'action': 'BUY',
                'quantity': self.position_size,
                'price': data['Close'].iloc[index],
                'timestamp': str(data.index[index])
            }
        return None

def main():
    # Generate data
    data = DataHandler.generate_sample_data(days=100, initial_price=50.0)
    
    # Compare strategies
    strategies = [
        BuyAndHoldStrategy(position_size=100),
        SimpleMovingAverageStrategy(short_window=10, long_window=30, position_size=100)
    ]
    
    for strategy in strategies:
        print(f"\n{'='*50}")
        engine = BacktestEngine(initial_cash=5000.0)
        results = engine.run_backtest(data, strategy, symbol="TEST")

if __name__ == "__main__":
    main()