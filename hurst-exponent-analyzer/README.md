# 📊 Hurst Exponent Market Regime Analyzer (`hurst_analyzer.py`)

A quantitative Python implementation to estimate the **Hurst Exponent ($H$)** on financial time series using empirical variance scaling analysis over variable lag structures.

---

## 🔬 Mathematical Formulation

The Hurst Exponent evaluates the long-term memory and fractal structure of a time series. It classifies asset price series into **Mean-Reverting**, **Random Walk**, or **Persistent Trending** regimes.

### 1. Standard Deviation Scaling ($\sigma$)
For each lag $\tau \in [2, \text{max lag}]$, pairwise price differences are evaluated:

$$\Delta X_\tau = X_{t+\tau} - X_t$$

The standard deviation of these differences scales as a power-law function of the lag:

$$\sigma(\tau) = \text{std}(\Delta X_\tau) \propto \tau^H$$

### 2. Log-Log Linear Regression
Taking the natural logarithm of both sides transforms the power-law into a linear equation:

$$\ln(\sigma(\tau)) = H \cdot \ln(\tau) + C$$

Applying Ordinary Least Squares (OLS) regression via `np.polyfit()` on $\ln(\sigma(\tau))$ versus $\ln(\tau)$ extracts the slope parameter, which represents **$H$**.

---

## 📈 Quantitative Regime Classification

- **$H < 0.5$ (Anti-persistent / Mean-Reverting):** High-frequency fluctuation; prices tend to revert to their historical average.
- **$H = 0.5$ (Geometric Brownian Motion):** Pure memoryless Brownian motion (Random Walk).
- **$H > 0.5$ (Persistent / Trending):** Long-memory dynamics; past price movement directionally dictates future path.

---

## 💻 Source Code (`hurst_analyzer.py`)

```python
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def get_hurst_ind(ts, max_lag):

    lages=range(2,max_lag)
    tau=[]

    for lag in lages:


        diff=ts[lag:] - ts[:-lag]

        std_d=np.std(diff)

        tau.append(std_d)


    hurst_ex=np.polyfit(np.log(lages),np.log(tau),1)[0]
    return hurst_ex

ticker=yf.Ticker("AAPL")
df=ticker.history(period="1y")

lages_list=[20,
            100,
            200,
            500]

for lag in lages_list:
    hurst_exp=get_hurst_ind(df["Close"].values,lag)

    print(f"Hurst exponent with {lag} lags: {hurst_exp:.4f}")
