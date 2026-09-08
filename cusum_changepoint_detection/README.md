# 📉 CUSUM Time-Series Changepoint Detection (`cusum_changepoint_detection.py`)

A Python quantitative module implementing the **Cumulative Sum (CUSUM)** algorithm to detect structural regime shifts and mean shifts in financial time-series data (e.g., Apple stock prices `AAPL`).

Changepoint detection identifies critical time points where the underlying probability distribution or statistical properties (such as the empirical mean) of a financial asset undergo a structural shift.

---

## 📐 Mathematical Formulation

The CUSUM algorithm evaluates shifts in the process mean $\mu$ across an $N$-length price series $P = \{p_1, p_2, \dots, p_N\}$.

### 1. Empirical Mean Computation
$$\bar{\mu} = \frac{1}{N} \sum_{i=1}^{N} p_i$$

### 2. Cumulative Deviation Trajectory ($S_k$)
The cumulative sum sequence $S_k$ aggregates mean-centered price residuals up to time $k$:
$$S_k = \sum_{i=1}^{k} (p_i - \bar{\mu}), \quad \text{for } k = 1, 2, \dots, N$$

By definition, $S_0 = 0$ and $S_N = 0$.

### 3. Changepoint Identification ($k^*$)
The structural shift corresponds to the index $k^*$ where the absolute deviation of $S_k$ is maximized:
$$k^* = \arg\max_{1 \le k \le N} |S_k|$$

The date associated with index $k^*$ indicates the point of maximum regime shift in the time series.

---

## 🛠️ Code Architecture & Logic

1. **Data Ingestion:** Downloads historical daily close prices using `yfinance` and strips multi-index headers.
2. **Mean Centering:** Subtracts the global sample mean $\bar{\mu}$ from each daily close price.
3. **Accumulation (`np.cumsum`):** Constructs the continuous deviation path $S_k$.
4. **Argmax Extraction (`np.argmax`):** Pinpoints the single timestamp corresponding to $\max |S_k|$.
5. **Dual Visual Analysis:** Plots both the asset price trajectory with the vertical changepoint indicator and the underlying CUSUM curve.

---

## 💻 Dependencies & Setup

Install required libraries:
```bash
pip install numpy pandas yfinance matplotlib
