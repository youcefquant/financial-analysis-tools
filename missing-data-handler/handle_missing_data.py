import yfinance as yf
import pandas as pd
import numpy as np
#Download data
stock1=yf.download("AAPL",
                  start="2020-01-01",
                  end="2026-01-01")
#Changing the column name to simplify the process and organization
df=stock1[["Close"]].rename(columns={"Close":"Cpi"})
#Install randomness
np.random.seed(42)
history1=np.random.choice(df.index,
                          5,
                          replace=False)

df["cpi_missing"]=df.loc[:, "Cpi"]
df.loc[history1,"cpi_missing"]=np.nan
df[df["cpi_missing"].isna()]

#Fill in the values
df["method_ffill"] = df["cpi_missing"].ffill()
df["method_bfill"] = df["cpi_missing"].bfill()
df[df["cpi_missing"].isna()]
#Draw values

df.loc["2023-01-01":"2026-01-01"].drop(columns=["cpi_missing"]).plot(title="Different ways of filling missing values",figsize=(25,10),linewidth=3)
plt.grid(True)
plt.show()


