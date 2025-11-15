import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf

ticker = st.selectbox("Ticker", ["AAPL", "TSLA", "NVDA"])

data = yf.download(ticker, period="1y", interval="1d", progress=False)

fig, ax = plt.subplots(figsize = (10,5))
ax.plot(data["Close"])
ax.set_title(ticker)
st.pyplot(fig)
