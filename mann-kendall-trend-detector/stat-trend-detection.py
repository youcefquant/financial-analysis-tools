import pandas as pd
import numpy as np
import yfinance as yf
import pymannkendall as mk
ticker=yf.Ticker("AAPL")
df=ticker.history(period="6mo")

df.columns=df.columns.get_level_values(0)
price=df["Close"].squeeze()

def get_tau(window):
    return mk.original_test(window).Tau

tau_valu=price.rolling(30).apply(get_tau,raw=False)
pricef_F=tau_valu[tau_valu>=0.7].index

plt.figure(figsize=(10,5))
plt.plot(price.index,
         price.values,
         color="blue",
         label="AAPL Stock")
for pi in pricef_F:
    plt.axvline(x=pi,
                color="red",
                alpha=0.5)
plt.grid(True)
plt.show()
