# 📈 Non-Parametric Trend Detection in Financial Time Series

An implementation of the **Mann-Kendall Statistical Test** to identify monotonic trends in equity price series without relying on lagged technical indicators. Built using Python, Pandas vectorized rolling functions, and `pymannkendall`.

---

## 🔬 Core Concept

Traditional momentum indicators (RSI, Moving Averages) suffer from lag and curve-fitting issues. This repository utilizes the **Mann-Kendall (MK) Test**—a non-parametric statistical evaluation—to measure the continuous directionality and monotonicity of price movement over a sliding $N$-day time frame ($N=30$).

### Key Metric: Kendall's Tau ($\tau$)
- **$\tau = 1.0$**: Perfect monotonic upward trend across the window.
- **$\tau = 0.0$**: Random walk / No clear trend.
- **Threshold Condition**: A signal is validated only when $\tau \ge 0.7$, ensuring high statistical confidence and eliminating market noise.

---

## 🛠 Tech Stack & Dependencies

- **Language:** Python 3.10+
- **Data Source:** `yfinance`
- **Data Manipulation:** `pandas` (Vectorized `.rolling()` execution)
- **Statistical Engine:** `pymannkendall`
- **Visualization:** `matplotlib`

---

## 🚀 Execution & Quickstart

```bash
# Clone repository
git clone [https://github.com/YOUR_USERNAME/mann-kendall-trend-detector.git](https://github.com/YOUR_USERNAME/mann-kendall-trend-detector.git)
cd mann-kendall-trend-detector

# Install dependencies
pip install pandas yfinance pymannkendall matplotlib

# Run the detector
python trend_detector.py
