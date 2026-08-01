import numpy as np
import pandas as pd
import yfinance as yf
import seaborn as sns

df=yf.download("AAPL"
               ,start="2022-01-01"
               ,end="2026-07-01",
               progress=False)
df[["Close"]].copy()
df["simple_rtn"]=df["Close"].pct_change()
df["year"]=df.index.year
df["month"]=df.index.month
sns.lineplot(data=df,
             x="month",
             y="simple_rtn",
             hue="year",
             style="year",
             palette="tab10",
             errorbar=None
             )
plt.title("Return price vs month")
plt.show()
