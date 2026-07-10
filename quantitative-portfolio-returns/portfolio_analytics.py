# Calculating logarithmic and simple returns adjusted for inflation.
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr

stock = yf.download("NVDA", start="2026-01-01", end="2026-06-13", interval="1mo")

cpi = pdr.get_data_fred("CPIAUCSL", start="2026-01-01", end="2026-06-13")

df = stock.iloc[:, [0]].copy()
df.columns = ["Close"]

df = df.join(cpi, how="left")
df.rename(columns={"CPIAUCSL": "CPI_value"}, inplace=inplace:=True)

df["sp_rtn"] = df["Close"].pct_change(fill_method=None)
df["invlo_rtn"] = df["CPI_value"].pct_change(fill_method=None)

print(df.head())
