import streamlit as st
from financeinfo import fetch
from backtesting import run_backtest
from plotter import get_fig

def main():
    tickers = ["AAPL", "NVDA", "TSLA"]
    ticker = st.selectbox("Select a ticker",
                        tickers,
                        index=None)

    if ticker:
        data = fetch(ticker)
        fig = get_fig(data,ticker)
        st.pyplot(fig)

if __name__ == "__main__":
    main()    
