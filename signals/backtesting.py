import pandas as pd

# long only backtest
def run_backtest(data: pd.DataFrame, signal_column: str):
    capital = 100 # % of starting capital
    share_value = 0 # % of starting capital in stock

    def buy(x):
        capital -= x
        share_value += x

    def sell(x):
        share_value -= x
        capital += x

    bullish = data[signal_column] == 1
    bearish = data[signal_column] == -1

    # because of crossovers, if there are n buys there are between n-1 and n+1 sells
    buydates = data.index[bullish]
    selldates = data.index[bearish]
    selldates = selldates[selldates > buydates[0]] # first sell happens after a buy
    buydates = buydates[buydates < selldates[-1]] # last buy happens before a sell

    trades = pd.DataFrame({
        "Buy Date": buydates,
        "Buy Price": data.loc(buydates, "Close"), # prices when buys occur
        "Sell Date": selldates,
        "Buy Price": data.loc(selldates, "Close") # prices when sells occur
    })

    returns = trades["Sell Price"] / trades["Buy Price"] - 1
    print(returns) 

    