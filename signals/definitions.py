import indicators.compute as indct
from enum import Enum

class IndicatorType(str, Enum):
    OVERLAY = "overlay"
    OSCILLATOR = "oscillator"

# map the indicator names to their corresponding functions and type
# overlay can be plotted on the graph normally
# oscillator needs a subplot
INDICATORS = {
    "SMA20": {
        "fn": lambda d: indct.compute_sma(d["Close"], 20),
        "type": IndicatorType.OVERLAY
    },
    "SMA50": {
        "fn": lambda d: indct.compute_sma(d["Close"], 50),
        "type": IndicatorType.OVERLAY
    },
    "EMA9": {
        "fn": lambda d: indct.compute_ema(d["Close"], 9),
        "type": IndicatorType.OVERLAY
    },
    "EMA21": {
        "fn": lambda d: indct.compute_ema(d["Close"], 21),
        "type": IndicatorType.OVERLAY
    },
    "MACD": {
        "fn": lambda d: indct.compute_macd(d["Close"]),
        "type": IndicatorType.OSCILLATOR
    },
    "RSI": {
        "fn": lambda d: indct.compute_rsi(d["Close"], 14),
        "type": IndicatorType.OSCILLATOR
    },
    "STOCHASTIC": {
        "fn": lambda d: indct.compute_stochastic(d["High"], d["Low"], d["Close"], k_period=14, d_period=3),
        "type": IndicatorType.OSCILLATOR
    },
    "ATR": {
        "fn": lambda d: indct.compute_atr(d["High"], d["Low"], d["Close"], 14),
        "type": IndicatorType.OSCILLATOR
    },
    "BOLLINGER BANDS": {
        "fn": lambda d: indct.compute_bbands(d["Close"], period=20, num_std=2),
        "type": IndicatorType.OVERLAY
    },
    "OBV": {
        "fn": lambda d: indct.compute_obv(d["Close"], d["Volume"]),
        "type": IndicatorType.OSCILLATOR
    },
}

# indicators where crossovers are meaningful (ax_name, fast, slow)
CROSSOVER_PAIRS = [
    ("MAIN","SMA20", "SMA50"),
    ("MAIN","EMA9", "EMA21"),
    ("MACD","MACD", "Signal"),
    ("STOCHASTIC","STOCH_%K", "STOCH_%D")
]

VALID_INTERVALS = {
    "1d":  ["1m", "2m", "5m", "15m", "30m", "1h"],
    "5d":  ["1m", "2m", "5m", "15m", "30m", "1h"],
    "1mo": ["5m", "15m", "30m", "1h", "1d"],
    "3mo": ["1d", "1wk", "1mo"],
    "6mo": ["1d", "1wk", "1mo"],
    "1y":  ["1d", "1wk", "1mo"],
    "5y":  ["1wk", "1mo"],
    "10y": ["1mo"],
    "YTD": ["1d", "1wk", "1mo"],
    "Max": ["1mo"], 
}