import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
ticker=yf.Ticker("AAPL")
df=ticker.history(period="1y")

df.columns=df.columns.get_level_values(0)

date=df.index
price=df["Close"].dropna().values
date=date[:len(price)]

men=np.mean(price)
cusume=np.cumsum(price-men)

changespointes_index=np.argmax(np.abs(cusume))
changespointes_date=date[changespointes_index]

plt.figure(figsize=(10,5))
plt.plot(date,
         price,
         color="blue",
         label="AAPL Stock")
plt.axvline(x=changespointes_date,
            label="Cumulative Return",
            color="red",
            linestyle="--",
            linewidth=2)
plt.legend()
plt.show()
