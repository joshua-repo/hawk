"""Example of creating a custom strategy"""

from hawk.data import DataHandler
from hawk.engine import BacktestEngine
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
                "action": "BUY",
                "quantity": self.position_size,
                "price": data["Close"].iloc[index],
                "timestamp": str(data.index[index]),
            }
        return None


def main():
    # Generate data
    data_handler = DataHandler()
    data = data_handler.generate_sample_data(days=100, initial_price=50.0)

    # Compare strategies
    strategies = [
        BuyAndHoldStrategy(position_size=100),
        SimpleMovingAverageStrategy(short_window=10, long_window=30, position_size=100),
    ]

    for strategy in strategies:
        print(f"\n{'=' * 50}")
        print(f"Testing strategy: {strategy.name}")
        engine = BacktestEngine(initial_cash=5000.0)
        results = engine.run_backtest(data, strategy, symbol="TEST")

        # Print results
        print(f"Final value: ${results.get('final_value', 0):.2f}")
        print(f"Total trades: {len(results.get('trades', []))}")


if __name__ == "__main__":
    main()
