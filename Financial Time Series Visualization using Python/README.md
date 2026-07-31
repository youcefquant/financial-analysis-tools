📈 Financial Time Series & Returns Visualization
A clean and modular Python implementation for fetching stock market data, 
calculating financial returns,
and visualizing time series metrics using Pandas, Matplotlib, and Plotly.

📌 Overview
This project demonstrates how to process financial data and structure standard financial charts. It covers:

Fetching historical stock prices automatically via Yahoo Finance (yfinance).

Calculating Simple Returns and Logarithmic Returns.

Creating multi-panel, synchronized time-series plots using Matplotlib’s Object-Oriented API (fig, ax).

Generating interactive price dashboards using Plotly.

🛠️ Key Features & Code Logic
Object-Oriented Plotting (fig, ax):
Uses plt.subplots(nrows, ncols, sharex=True) to decouple layout management from data processing, ensuring full control over each subplot's axis, labels, and formatting.

Synchronized Time Axes (sharex=True):
Aligns price movements and daily return volatility vertically across time, eliminating duplicate date labels and making visual correlation seamless.

Multi-Backend Visualization:
Supports both static publication-ready charts (Matplotlib) and dynamic, interactive graphs (Plotly).
