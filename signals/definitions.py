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
}

# indicators where crossovers are meaningful
CROSSOVER_PAIRS = [
    ("SMA20", "SMA50"),
    ("EMA9", "EMA21"),
    ("MACD", "Signal") # internal
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