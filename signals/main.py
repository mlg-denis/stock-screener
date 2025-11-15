import data
import indicators
import plot
import backtesting

def main():
    ticker = "TSLA"
    info = data.fetch(ticker)
    closes = info["Close"]

    sma20 = indicators.compute_sma(closes, 20)
    sma50 = indicators.compute_sma(closes, 50)
    ema12 = indicators.compute_ema(closes, 12)
    ema26 = indicators.compute_ema(closes, 26)
   
    column = "Crossover"
    info[column] = indicators.detect_crossovers(sma20, sma50)

    backtesting.run_backtest(info, column)

    plot.init()
    plot.plot_series(closes, "Price", "-", 0.7)
    plot.plot_series(ema12, "EMA12", "--", 0.35)
    plot.plot_series(ema26, "EMA26", "--", 0.35)
    plot.plot_crossovers(info, column)
    plot.title(ticker)
    plot.show()

if __name__ == "__main__":
    main()