# Portfolio Analytics & Real Returns 📊

This module focuses on evaluating asset performance by adjusting nominal market returns against inflation indicators using economic data from FRED (Federal Reserve Economic Data).

---

## 🎯 Purpose

Calculating nominal returns of a stock often gives an incomplete picture. This tool joins equity price data with the **Consumer Price Index (CPI)** to prepare dataset structures for **Inflation-Adjusted Real Returns** analysis.

---

## 📦 Data Sources

* **Stock Data:** Yahoo Finance (`NVDA` - Monthly Interval).
* **Economic Data:** Federal Reserve Bank of St. Louis (`CPIAUCSL` - Consumer Price Index for All Urban Consumers).

---

## 💻 Code Overview

```python
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf

# Fetch Stock and CPI Data
stock = yf.download("NVDA", start="2026-01-01", end="2026-06-13", interval="1mo")
cpi = pdr.get_data_fred("CPIAUCSL", start="2026-01-01", end="2026-06-13")

# Merge Datasets
df = stock.iloc[:, [0]].copy()
df.columns = ["Close"]
df = df.join(cpi, how="left")
df.rename(columns={"CPIAUCSL": "CPI_value"}, inplace=True)

# Calculate Stock Returns vs Inflation Rate
df["sp_rtn"] = df["Close"].pct_change(fill_method=None)
df["inf_rtn"] = df["CPI_value"].pct_change(fill_method=None)
