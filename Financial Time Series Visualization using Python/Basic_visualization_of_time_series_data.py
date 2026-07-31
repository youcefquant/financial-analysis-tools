import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

df=yf.download("AAPL",start="2026-01-01",
               end="2026-07-01",
               progress=False)
df["Close"].copy()
df["simple_rtn"]=df["Close"].pct_change()

df["simple_rtn"].head()

fig, ax=plt.subplots(2,1 ,sharex=True)
df["Close"].plot(ax=ax[0])
ax[0].set(title="Close price",
          ylabel="Price ($)")
df["simple_rtn"].plot(ax=ax[1])
ax[1].set(title="simple rtn "
          ,ylabel="Price ($)")
plt.show()
