# AAPL Stock Outlier Detection via Hampel Filter 📈

This repository provides a robust statistical approach to detecting price anomalies (outliers) in financial time series data using the **Hampel Filter**. The project pulls historical data for Apple Inc. (`AAPL`) using `yfinance`, applies median-based statistical methods, and visualizes the detected anomalies.

---

## 📐 Mathematical Foundation

Unlike traditional $3\sigma$ (3-Sigma) moving thresholds that rely on the sample mean ($\mu$) and standard deviation ($\sigma$), the **Hampel Filter** uses **Robust Statistics** based on the **Median** and **Median Absolute Deviation (MAD)**. This prevents extreme price shocks from distorting the rolling statistics (avoiding the *Ghost Effect*).

### 1. Rolling Median
For a centered window $W$ of size $N$ around observation $x_i$:

$$\text{Median}_t = \text{median}(x_{t-k}, \dots, x_t, \dots, x_{t+k})$$

### 2. Median Absolute Deviation (MAD)
Measures the statistical dispersion of the window around its median:

$$\text{MAD}_t = \text{median}\left( \vert{}x_i - \text{Median}_t\vert{} \right) \quad \text{for } i \in W$$

### 3. Consistency Scale Factor ($k$)
To make the MAD a consistent estimator of the standard deviation ($\sigma$) under a normal (Gaussian) distribution, it is scaled by a constant factor $k \approx 1.4826$:

$$\sigma_{\text{estimated}} = 1.4826 \times \text{MAD}_t$$

### 4. Outlier Threshold Condition
An observation $x_t$ is flagged as an outlier ($\text{Outlier}_t = \text{True}$) if its absolute deviation from the median exceeds $n$ scaled standard deviations (default $n = 3$):

$$\vert{}x_t - \text{Median}_t\vert{} > 3 \times \sigma_{\text{estimated}}$$

---

## 💻 Python Implementation

```python
import matplotlib.pyplot as plt
from sktime.transformations.series.outlier_detection import HampelFilter
import yfinance as yf

# 1. Download 1 year of AAPL historical stock data
ticker = yf.Ticker("AAPL")
df = ticker.history(period="1y")

# 2. Initialize and apply the Hampel Filter on Close Prices
hampel_filter = HampelFilter(window_length=20, return_bool=True)
df["outlier"] = hampel_filter.fit_transform(df["Close"])

# 3. Visualization
fig, ax = plt.subplots(figsize=(10, 5))

# Plot AAPL Close Price
df["Close"].plot(ax=ax, color="red", label="AAPL Close Price", alpha=0.8)

# Highlight Outliers
ax.scatter(
    df[df["outlier"]].index,
    df.loc[df["outlier"], "Close"],
    color="blue",
    label="Outlier (Hampel)",
    zorder=5,
)

# Formatting
ax.set_title("AAPL Stock Price - Outlier Detection via Hampel Filter")
plt.tight_layout()
plt.show()
