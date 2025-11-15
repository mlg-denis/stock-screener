import pandas as pd

# long only backtest
def run_backtest(data: pd.DataFrame, signal_column: str):
    bullish = data[signal_column] == 1 # positive crossover
    bearish = data[signal_column] == -1 # negative crossover

    buydates = data.index[bullish]
    selldates = data.index[bearish]
    selldates = selldates[selldates > buydates[0]] # first sell happens after a buy
    buydates = buydates[buydates < selldates[-1]] # last buy happens before a sell
    n = min(len(buydates), len(selldates))
    if (n == 0):
        print ("No trades found")
        return
    buydates, selldates = buydates[:n], selldates[:n] # truncate to ensure pairings - redundant when using crossovers because they will be off by at most 1

    # drop the old date index to align by order instead of date label
    buyprices = data.loc[buydates, "Close"].reset_index(drop=True)
    sellprices = data.loc[selldates, "Close"].reset_index(drop=True)

    trades = pd.DataFrame({
        "Buy Date": buydates,
        "Buy Price": buyprices,
        "Sell Date": selldates,
        "Sell Price": sellprices,
        "Return": sellprices / buyprices - 1 # rate of return
    })
    print(trades)

    