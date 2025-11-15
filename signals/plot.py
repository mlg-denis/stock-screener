import matplotlib.pyplot as plt
import pandas as pd

signal_size = 100

def init():
    plt.figure(figsize= (10,5))
    plt.xlabel("Date")
    plt.ylabel("Price")

def plot_series(series: pd.Series, label: str, style: str = "-", alpha: float = 1):
    plt.plot(series, style, label = label, alpha = alpha)

def plot_crossovers(data: pd.DataFrame, column: str):
    # takes all the dates (and the prices @ close on those dates) where a crossover
    # has occurred and plots a scatter plot with a marker for the bullish signal
    plt.scatter(
        data.index[data[column] == 1],
        data["Close"][data[column] == 1],
        marker = "^", color = "green", s = signal_size, label = "Bullish Crossover"
    )

    # same as above but for bearish signals
    plt.scatter(
        data.index[data[column] == -1],
        data["Close"][data[column] == -1],
        marker = "v", color = "red", s = signal_size, label = "Bearish Crossover"
    )

def title(title):
    plt.title(title)

def show():
    plt.legend()
    plt.show()    