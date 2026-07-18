"""Base strategy class"""

from typing import Dict, Optional

import pandas as pd


class BaseStrategy:
    """Base class for trading strategies"""

    def __init__(self, name: str = "BaseStrategy"):
        self.name = name

    def generate_signal(self, data: pd.DataFrame, index: int) -> Optional[Dict]:
        """
        Generate trading signal based on data

        Args:
            data: Price data DataFrame
            index: Current data index

        Returns:
            Dict with signal info or None
        """
        raise NotImplementedError("Subclasses must implement generate_signal")


class SimpleMovingAverageStrategy(BaseStrategy):
    """Simple moving average crossover strategy"""

    def __init__(
        self, short_window: int = 20, long_window: int = 50, position_size: int = 100
    ):
        super().__init__(f"SMA({short_window},{long_window})")
        self.short_window = short_window
        self.long_window = long_window
        self.position_size = position_size
        self.position = 0  # Track current position

    def generate_signal(self, data: pd.DataFrame, index: int) -> Optional[Dict]:
        if index < self.long_window:
            return None

        # Calculate moving averages
        short_ma = data["Close"].iloc[index - self.short_window + 1 : index + 1].mean()
        long_ma = data["Close"].iloc[index - self.long_window + 1 : index + 1].mean()
        prev_short_ma = data["Close"].iloc[index - self.short_window : index].mean()
        prev_long_ma = data["Close"].iloc[index - self.long_window : index].mean()

        current_price = data["Close"].iloc[index]

        # Buy signal: short MA crosses above long MA
        if prev_short_ma <= prev_long_ma and short_ma > long_ma and self.position == 0:
            self.position = self.position_size
            return {
                "action": "BUY",
                "quantity": self.position_size,
                "price": current_price,
                "timestamp": str(data.index[index]),
            }

        # Sell signal: short MA crosses below long MA
        elif prev_short_ma >= prev_long_ma and short_ma < long_ma and self.position > 0:
            quantity = self.position
            self.position = 0
            return {
                "action": "SELL",
                "quantity": quantity,
                "price": current_price,
                "timestamp": str(data.index[index]),
            }

        return None
