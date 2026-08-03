# Missing Data Handling in Time Series 🧩

This module demonstrates techniques for simulating and handling missing values (NaNs) in financial time series without introducing data leakage or distortion.

---

## 💡 Overview

In quantitative finance, missing data can break mathematical models and backtests. This script simulates missing market data and compares two fundamental imputation methods:

* **Forward Fill (`ffill`):** Propagates the last valid observation forward. *(Preferred for real-time trading models to avoid look-ahead bias)*.
* **Backward Fill (`bfill`):** Uses the next valid observation to fill the gap backward.

---

## 🛠 Simulated Missing Data Logic

```python
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Randomly drop 5 dates from the dataset
history1 = np.random.choice(df.index, 5, replace=False)
df.loc[history1, "cpi_missing"] = np.nan
