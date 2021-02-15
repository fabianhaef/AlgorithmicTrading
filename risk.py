import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import seaborn

stock_tickers = ['APHA', 'TSLA', 'AMZN', 'AAPL']
stocks = yf.download(stock_tickers, start="2018-01-01", end="2021-01-31")
data = stocks.loc[:, "Close"].copy()


#Normalizing Values by 100
normalized_data = data.div(data.iloc[0]).mul(100)
#apha = normalized_data.APHA.copy().to_frame()


com = normalized_data.pct_change().dropna()
sum = com.describe().T.loc[:, ["mean", "std"]]

sum["mean"] = sum["mean"]*252
sum["std"] = sum["std"] * np.sqrt(252)


sum.plot.scatter(x="std", y="mean", figsize= (12,8), s=50, fontsize=15)
for i in sum.index:
    plt.annotate(i, xy=(sum.loc[i, "std"]+0.002, sum.loc[i, "mean"]+0.002), size = 15)

#ret.plot(kind="hist", figsize=(17, 8), bins=100)
plt.style.use("seaborn")
plt.show()