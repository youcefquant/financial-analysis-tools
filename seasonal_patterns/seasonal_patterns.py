from statsmodels.graphics.tsaplots import month_plot
import matplotlib.pyplot as plt

monthly_rtn=df["simple_rtn"].dropna().resample("ME").mean().to_period("M")
fig, ax =plt.subplots(figsize=(15,5))
month_plot(monthly_rtn,ax=ax)
plt.title("rutern monthly")
plt.grid(True,alpha=0.5)
plt.show()
