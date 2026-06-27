"""Basic backtest example"""
import os

from hawk.engine import BacktestEngine
from hawk.data import DataHandler
from hawk.strategy import SimpleMovingAverageStrategy

def main():
    # Generate sample data
    print(f"Python PID: {os.getpid()}")
    print("📊 Generating sample data...")
    data_handler = DataHandler()
    data = data_handler.generate_sample_data(days=252, initial_price=100.0)
    
    # Create strategy
    strategy = SimpleMovingAverageStrategy(short_window=20, long_window=50, position_size=100)
    
    # Run backtest
    engine = BacktestEngine(initial_cash=10000.0)
    results = engine.run_backtest(data, strategy, symbol="SAMPLE")
    
    # Show some trades
    if results['trades']:
        print(f"\n📋 First 5 trades:")
        for i, trade in enumerate(results['trades'][:5]):
            print(f"  {i+1}. {trade.action} {trade.quantity} @ ${trade.price:.2f} on {trade.timestamp[:10]}")

if __name__ == "__main__":
    main()