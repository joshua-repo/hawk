"""Hawk Trading Engine - Minimized Learning Version"""

__version__ = "1.0.0"

from .engine import BacktestEngine
from .strategy import BaseStrategy
from .data import DataHandler

__all__ = ['BacktestEngine', 'BaseStrategy', 'DataHandler']