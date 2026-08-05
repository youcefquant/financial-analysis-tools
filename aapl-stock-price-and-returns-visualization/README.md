# AAPL Stock Price & Simple Return Visualization

An interactive visualization tool built with Python to analyze **Apple Inc. (AAPL)** daily stock performance. This project fetches historical market data using `yfinance` and generates interactive subplots for both daily closing prices and simple daily returns using `Plotly Express`.

## Features
* **Automated Data Retrieval:** Downloads historical price data directly from Yahoo Finance.
* **MultiIndex Column Handling:** Cleanly flattens DataFrame headers to prevent library conflicts.
* **Financial Calculations:** Calculates daily percentage change (Simple Return) via Pandas.
* **Interactive Subplots:** Displays Close Price and Daily Returns in separate, unlinked y-axes for accurate scaling.

## Requirements
Make sure you have the following Python packages installed:

```bash
pip install pandas yfinance plotly

