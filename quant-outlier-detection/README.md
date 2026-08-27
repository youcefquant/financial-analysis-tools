# 📈 Quantitative Outlier Detection using Rolling 3-Sigma Rule

A Python-based quantitative finance toolkit designed to detect, visual, and clean statistical anomalies in stock return time series using dynamic rolling boundaries.

---

## 📌 Mathematical Foundation

In financial quantitative analysis, raw asset prices $P_t$ are non-stationary. To make the data suitable for statistical modeling, we compute the **daily percentage returns** $R_t$:

$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$$

### Dynamic 3-Sigma Thresholding
Instead of using fixed standard deviations across the entire dataset (which fails to account for market volatility clustering), we compute a **21-day rolling window** mean ($\mu_t$) and standard deviation ($\sigma_t$):

$$\mu_t = \frac{1}{21} \sum_{i=0}^{20} R_{t-i}$$

$$\sigma_t = \sqrt{\frac{1}{20} \sum_{i=0}^{20} (R_{t-i} - \mu_t)^2}$$

The upper and lower statistical boundaries are then defined dynamically as:

$$\text{Upper}_t = \mu_t + 3\sigma_t$$

$$\text{Lower}_t = \mu_t - 3\sigma_t$$

### Outlier Condition
According to the **Empirical Rule**, assuming approximately normally distributed returns, $99.73\%$ of observations lie within $\pm 3\sigma$. An observation $R_t$ is flagged as a statistical outlier if:

$$\text{Outlier}_t = \left( R_t > \text{Upper}_t \right) \lor \left( R_t < \text{Lower}_t \right)$$

---

## 🚀 Key Features

- **Automated Data Retrieval:** Integrates with `yfinance` for seamless API access.
- **Dynamic Risk Bands:** Adapts to shifting market regimes via rolling window statistics.
- **Noise Isolation:** Isolates structural shocks (earnings announcements, black swan events) from natural market noise.
- **Publication-Ready Visualization:** Matplotlib integration with custom layering (`zorder`) for clean charting.

---

## 🛠️ Code Breakdown (`outlier_detector.py`)

Below is the complete logic implementing the quantitative pipeline:

```python
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# 1. Download Historical Data
ticker = "TSLA"
df = yf.download(ticker, start="2019-01-01", end="2020-12-31", progress=False)

# 2. Compute Daily Percentage Returns
df["rtn"] = df["Adj Close"].pct_change()
df = df[["rtn"]].copy()

# 3. Calculate Rolling Statistics (21-Day Trading Window)
df_rolling = df[["rtn"]].rolling(window=21).agg(["mean", "std"])
df_rolling.columns = df_rolling.columns.droplevel()
df = df.join(df_rolling)

# 4. Set Dynamic 3-Sigma Boundaries
N_SIGMAS = 3
df["upper"] = df["mean"] + N_SIGMAS * df["std"]
df["lower"] = df["mean"] - N_SIGMAS * df["std"]

# 5. Outlier Detection Mask
df["outlier"] = (df["rtn"] > df["upper"]) | (df["rtn"] < df["lower"])

# 6. Plotting Results
fig, ax = plt.subplots(figsize=(10, 6))
df[["rtn", "upper", "lower"]].plot(ax=ax)

# Scatter plot for flagged outliers only
ax.scatter(
    df[df["outlier"]].index,
    df.loc[df["outlier"], "rtn"],
    color="black",
    label="Outlier",
    zorder=5,
)

ax.set_title(f"{ticker} Stock Returns with Rolling 3-Sigma Outliers")
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
