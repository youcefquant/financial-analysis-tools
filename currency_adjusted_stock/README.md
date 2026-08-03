# FX Stock Converter & Currency Risk Analyzer 🔱💶

A quantitative tool for adjusting stock prices against foreign exchange (FX) rates, evaluating international portfolio returns and currency risk exposure.

---

## 🎯 Concept & Purpose

When investing in foreign equity markets, performance is determined by two factors:
1. **Asset Return:** Capital gain/loss of the stock itself.
2. **FX Return:** Fluctuations in the currency exchange rate.

This script converts **US Dollar ($USD)** denominated equities into **Euro (€EUR)** and plots equity returns alongside FX exposure to highlight currency risk.

---

## 🧮 Conversion Logic

1. **Invert FX Rate:**
   $$\text{Rate}_{\text{USD/EUR}} = \frac{1}{\text{EUR/USD}}$$

2. **Adjusted Asset Price:**
   $$\text{Price}_{\text{EUR}} = \text{Price}_{\text{USD}} \times \text{Rate}_{\text{USD/EUR}}$$

---

## 💻 Quick Code Usage

```python
import yfinance as yf

# Ingest Equities and FX Pairs
stock = yf.download("AAPL", start="2026-01-01", end="2026-07-01")
fx = yf.download("EURUSD=X", start="2026-01-01", end="2026-07-01")

# Convert Currency Base
df = stock[["Close"]].copy()
df["usd_to_eur"] = 1 / fx["Close"]
df["Close_EUR"] = df["Close"] * df["usd_to_eur"]
