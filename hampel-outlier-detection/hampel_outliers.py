import matplotlib.pyplot as plt
import yfinance as yf
from sktime.transformations.series.outlier_detection import HampelFilter

ticker=yf.Ticker("AAPL")
df=ticker.history(period="1y")

hampel_filter=HampelFilter(window_length=20,
                           return_bool=True)
df["outlier"]=hampel_filter.fit_transform(df["Close"])

fig ,ax=plt.subplots(figsize=(10,5))

df["Close"].plot(ax=ax,
                 color="red",
                 label="AAPL STOCK ",
                 alpha=0.7)
ax.scatter(df[df["outlier"]].index,
           df[df["outlier"]]["Close"],
           color="blue",
           label="AAPL STOCK ",
           zorder=5)
ax.set_title("AAPL STOCK Returns with Hampel Filter")
plt.tight_layout()
plt.show()
