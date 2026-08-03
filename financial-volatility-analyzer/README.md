# Financial Volatility Analyzer 📉⚡

A quantitative tool for calculating and annualizing **Realized Volatility (RV)** from intraday/daily log returns of financial assets.

---

## 📐 Mathematical Background

### 1. Daily Log Returns
Logarithmic returns are calculated as:
$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$

### 2. Realized Volatility (Monthly)
Realized volatility for a given month is computed as the square root of the sum of squared daily returns:
$$RV_{\text{monthly}} = \sqrt{\sum_{i=1}^{N} r_i^2}$$

### 3. Annualized Volatility
Using the **Square Root of Time Rule**, monthly volatility is scaled to an annual rate:
$$RV_{\text{annualized}} = RV_{\text{monthly}} \times \sqrt{12}$$

---

## 💻 Code Overview

```python
import numpy as np
import pandas as pd


# Realized Volatility Function
def calc_realized_vol(x):
    return np.sqrt(np.sum(x**2))


# Resample to Monthly and Annualize
df_rv = (
    df["log_rtn"]
    .groupby(pd.Grouper(freq="ME"))
    .apply(calc_realized_vol)
    .to_frame(name="monthly_vol")
)

df_rv["annualized_vol"] = df_rv["monthly_vol"] * np.sqrt(12)
