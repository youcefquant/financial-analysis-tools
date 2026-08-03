# Financial Analysis Tools 📈

A collection of Python tools for quantitative financial analysis and time series visualization.
This repository focuses on detecting seasonal patterns,
quarterly behavior,
and asset return dynamics.

---

## 🛠 Features

* **Monthly Seasonality Analysis:** Utilizing `statsmodels.graphics.tsaplots.month_plot` to identify historically strong and weak months.
* **Quarterly Performance Tracking:** Resampling daily financial data into quarterly periods (`QE`) to evaluate earnings-driven market behavior.
* **Polar Seasonal Visualizations:** Interactive 360-degree seasonal plots using `plotly.express` for continuous time-series pattern recognition.
* **Data Resampling & Processing:** Advanced handling of financial time series with Pandas and `yfinance`.

---

## 🚀 Built With

* **Python 3.x**
* **Pandas** & **NumPy**
* **Matplotlib** & **Seaborn**
* **Statsmodels**
* **Plotly Express**
* **yfinance**

---

## 💻 Quick Example

```python
from statsmodels.graphics.tsaplots import month_plot
import matplotlib.pyplot as plt

# Resample daily returns to monthly periods
monthly_rtn = df["simple_rtn"].dropna().resample("ME").sum().to_period("M")

# Plot monthly seasonal patterns
fig, ax = plt.subplots(figsize=(10, 5))
month_plot(monthly_rtn, ylabel="Monthly Returns", ax=ax)
plt.title("Asset Returns - Month Plot")
plt.grid(True, alpha=0.3)
plt.show()
