import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker=yf.Ticker("AAPL")
df=ticker.history(period="1y")
df["rtn"]=df["Close"].pct_change()
df=df[["rtn"]].copy()
df_rolling=df[["rtn"]].rolling(window=21).agg(["mean",
                                               "std"])
df_rolling.columns=df_rolling.columns.droplevel()
df=df.join(df_rolling)
sigma=3
df["upper"]=df["mean"]+sigma*df["std"]
df["lower"]=df["mean"]-sigma*df["std"]
df["outler"]=(df["rtn"]>df["upper"])|(df["rtn"]<df["lower"])

fig,ax=plt.subplots(figsize=(10,5))
df[["upper",
    "lower",
    "rtn"]].plot(ax=ax)

ax.scatter(df[df["outler"]].index,
           df.loc[df["outler"]]["rtn"],
           color="red",
           label="Outliers",
           zorder=5)
ax.set_title("AAPL Stock Returns with Rolling 3-Sigma Outliers")
plt.tight_layout()
plt.show()
