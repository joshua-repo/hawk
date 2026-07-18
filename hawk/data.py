"""Simple data handling"""

import numpy as np
import pandas as pd


class DataHandler:
    """Simple data handler for backtesting"""

    @staticmethod
    def load_csv(file_path: str) -> pd.DataFrame:
        """Load data from CSV file"""
        data = pd.read_csv(file_path)
        if "Date" in data.columns:
            data["Date"] = pd.to_datetime(data["Date"])
            data.set_index("Date", inplace=True)
        return data

    @staticmethod
    def generate_sample_data(
        days: int = 252, initial_price: float = 100.0
    ) -> pd.DataFrame:
        """Generate sample price data for testing"""
        dates = pd.date_range(start="2023-01-01", periods=days, freq="D")

        # Generate random walk
        returns = np.random.normal(
            0.0005, 0.02, days
        )  # Small positive drift with volatility
        prices = [initial_price]

        for ret in returns[1:]:
            prices.append(prices[-1] * (1 + ret))

        # Create OHLC data
        data = pd.DataFrame(
            {
                "Open": prices,
                "High": [p * (1 + abs(np.random.normal(0, 0.01))) for p in prices],
                "Low": [p * (1 - abs(np.random.normal(0, 0.01))) for p in prices],
                "Close": prices,
                "Volume": np.random.randint(100000, 1000000, days),
            },
            index=dates,
        )

        return data
