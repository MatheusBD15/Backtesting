from abc import ABCMeta, abstractmethod


class Strategy(object):
    """ Abstract base class that provides an interface for all subsequent trading strategies. 
    The goal of a (derived) Strategy object is to output a list of signals,
    which has the form of a time series indexed pandas DataFrame.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_signals(self):
        """Function that outputs the signals, either to long, hold or short. (1, 0, -1)"""

        raise NotImplementedError("Should implement generate_signals()!")

class Portfolio(object):
    """Abstract base class representing a portfolio of positions (cash and instruments)
    determined on the basis of a set of signals provided by a strategy"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_positions(self):
        """Provides the logic to determine how the portfolio 
        positions are allocated on the basis of forecasting
        signals and available cash."""

        raise NotImplementedError("Should implement generate_positions()!")

    @abstractmethod
    def backtest_portfolio(self):
        """Provides the logic to generate the trading orders
        and subsequent equity curve (i.e. growth of total equity),
        as a sum of holdings and cash, and the bar-period returns
        associated with this curve based on the 'positions' DataFrame.
        Produces a portfolio object that can be examined by 
        other classes/functions."""

        raise NotImplementedError("Should implement backtest_portfolio()!")

