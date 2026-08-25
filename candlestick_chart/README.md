# 📈 Candlestick Chart Visualizer (Dark Theme)

A Python-based quantitative finance tool designed to fetch historical stock data and visualize professional-grade candlestick charts with custom dark aesthetics and Technical Analysis indicators.

---

## ✨ Features

* **Data Acquisition**: Automatically retrieves dynamic historical stock market data using `yfinance`.
* **Custom Dark Theme**: Clean black background (`#000000`) with sleek grid styling for optimal visual contrast.
* **Technical Indicators**: Integrated Moving Averages (MA10 & MA20) overlay.
* **Volume Analysis**: Displays underlying trading volume bars synced with price action.
* **Robust Data Handling**: Automatically handles `MultiIndex` column formatting and runtime edge cases.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
   
## 💡 Why Plotly over Static Libraries?
Unlike static charting libraries (e.g., `matplotlib` or standard `mplfinance`), this implementation provides:
- Dynamic inspection of OHLC price data on hover.
- Fluid zooming and panning across different time horizons.
- Seamless weekend gap suppression for quantitative time-series analysis.
