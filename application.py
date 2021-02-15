import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

stock_tickers = ['AAPL', 'APHA', 'TLRY']
stocks = yf.download(stock_tickers, start="2019-01-01", end="2021-01-31")
data = stocks.loc[:, "Close"].copy()


#Normalizing Values by 100
normalized_data = data.div(data.iloc[0]).mul(100)

normalized_data.plot(figsize=(17, 8), fontsize=18)
plt.style.use("seaborn")
plt.show()