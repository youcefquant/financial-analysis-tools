import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock=yf.download("NVDA",
                  start="2024-01-01"
                  ,end="2026-01-01"
                  ,auto_adjust=True)
stock.columns=stock.columns.get_level_values(0)
df=stock[["Close"]].copy()
df["log_rtn"]=np.log(df["Close"]/df["Close"].shift(1))
df.dropna()

def vilz(x):
    return np.sqrt(np.sum(x**2))

df_rv=(

    df["log_rtn"].groupby(pd.Grouper(freq="M"))
    .apply(vilz)
    .to_frame(name="v_lo")  # تحويل السلسلة إلى DataFrame وتسمية العمود بـ v_lo
)

df_rv.rv=df_rv["v_lo"]*np.sqrt(12)

fig,ax=plt.subplots(2,1 ,figsize=(15,6),sharex=True)
ax[0].plot(df["log_rtn"], color="DodgerBlue",alpha=0.7)
ax[0].set_title("the log rtn in NVADA")
ax[1].plot(df_rv["v_lo"], color="DarkOrange",alpha=0.7)
ax[1].set_title("the v_ol in nvida")

plt.tight_layout()
plt.show()
