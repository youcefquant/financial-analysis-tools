import mplfinance as mpl
import plotly.graph_objects as go

ticker=yf.Ticker("AAPL")
df=ticker.history(period="1y")

fig=go.Figure(data=go.Candlestick(x=df.index,
                                  close=df["Close"],
                                  open=df["Open"],
                                  high=df["High"],
                                  low=df["Low"],
                                  ))
fig.update_layout(width=800,
                  height=600,
                  title="AAPL Candlestick")
fig.show()
