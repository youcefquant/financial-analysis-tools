import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

df=yf.download("AAPL",
               start="2026-01-01",
               end="2026-07-01",
               progress=False)

df=df[["Close"]].copy()
df.columns=["Close"]

df_fx=yf.download("EURUSD=X",
                  start="2026-01-01",
                  end="2026-07-01",
                  progress=False)

df["eur_usd"]=1/df_fx["Close"]
df["Close_eur"]=df["eur_usd"]*df["Close"]
df[["Close","eur_usd"]].plot(secondary_y="eur_usd",
                             figsize=(30,12),
                             linewidth=2)

plt.grid(True)
plt.show()
