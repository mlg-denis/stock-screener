import yfinance as yf
import pandas as pd

# get ticker data from yf, with default fallback params
# if ticker isn't found raise an exception
def fetch(ticker: str, period:str = "1y", interval:str = "1d", auto_adjust: bool = True) -> pd.DataFrame:
    try:
        return yf.download(ticker, period = period, interval = interval, auto_adjust=auto_adjust)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch {ticker}: {e}" )