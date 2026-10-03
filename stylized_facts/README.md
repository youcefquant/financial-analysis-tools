# 📉 Financial Return Normality & Fat-Tail Analyzer (`normality_analyzer.py`)

A quantitative Python diagnostic tool designed to test the **Log-Normal Returns Hypothesis** and visually detect **Fat-Tail Risks (Kurtosis)** in financial asset prices using Density Histograms and Quantile-Quantile (Q-Q) Plots.

---

## 🔬 Mathematical First Principles

Standard financial portfolio theory (e.g., Markowitz, Black-Scholes) assumes asset returns follow a normal distribution. This script tests whether empirical market returns violate this assumption.

### 1. Logarithmic Return Calculation
For price series $P_t$, continuous log returns are calculated as:

$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) = \ln(P_t) - \ln(P_{t-1})$$

### 2. Normal Probability Density Function (PDF)
Empirical parameters $\mu$ (mean) and $\sigma$ (standard deviation) are estimated to build the theoretical Gaussian curve:

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left( \frac{x - \mu}{\sigma} \right)^2}$$

### 3. Q-Q Plot Diagnostic
Plots empirical quantiles against theoretical normal quantiles. Deviations at the extremities indicate **Heavy-Tailed Behavior (Fat Tails)**, proving that extreme market events occur far more frequently than predicted by a standard normal model.

---

## 💡 Key Takeaways

- **Center Alignment:** Evaluates if asset volatility centers around the mean $\mu$.
- **Tail Extremities:** Outliers breaking off the Q-Q straight line confirm tail risk and high kurtosis, making standard standard deviation models underestimate true risk.

---

## 💻 Source Code (`normality_analyzer.py`)

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs
import seaborn as sns
import statsmodels.api as sm
import yfinance as yf

# 1. Fetch Market Data
df = yf.download(
    "AAPL",
    start="2025-01-01",
    end="2026-01-01",
    progress=True,
    multi_level_index=False,
)

# 2. Format DataFrame & Calculate Log Returns
df = df[["Close"]].rename(columns={"Close": "price"})
df["rtn_log"] = np.log(df["price"] / df["price"].shift(1))
df = df.dropna()

# 3. Parametric Normal Curve Estimation
r_range = np.linspace(min(df["rtn_log"]), max(df["rtn_log"]), num=100)
mun = df["rtn_log"].mean()
sigma = df["rtn_log"].std()
norm_pdf = scs.norm.pdf(r_range, loc=mun, scale=sigma)

# 4. Visualization
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# Density Histogram vs. Theoretical Normal PDF
sns.histplot(
    df["rtn_log"], stat="density", ax=ax[0], color="skyblue", alpha=0.6
)
ax[0].plot(r_range, norm_pdf, "g-", lw=2)
ax[0].set_title("Distribution of Asset Returns", fontsize=16)

# Quantile-Quantile (Q-Q) Plot
sm.qqplot(df["rtn_log"].values, line="s", ax=ax[1])
ax[1].set_title("Q-Q Plot vs. Normal Distribution", fontsize=16)

plt.tight_layout()
plt.show()
