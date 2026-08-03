# Financial Data Scraper 🌐📊

A multi-source data ingestion pipeline built in Python to retrieve market prices and macroeconomic indicators using financial APIs.

---

## 📡 Data Sources Integrated

1. **Yahoo Finance (`yfinance`):** Used for fetching daily OHLCV (Open, High, Low, Close, Volume) stock data.
2. **FRED (Federal Reserve Bank of St. Louis):** Used via `pandas_datareader` to ingest economic data such as the Consumer Price Index (CPI).
3. **Nasdaq Data Link (Quandl):** Utilized for deep historical market datasets and fundamental financial data.

---

## 🔐 Setup & API Key Requirement

To use the Nasdaq Data Link scraper, you need an API key from [Nasdaq Data Link](https://data.nasdaq.com/):

```python
import nasdaqdatalink

nasdaqdatalink.ApiConfig.api_key = "YOUR_ACTUAL_API_KEY"
