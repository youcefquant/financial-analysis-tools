import mplfinance as mpf
import pandas as pd
import yfinance as yf

df = yf.download("AAPL",
                 period="6mo", 
                 progress=False)

if isinstance(df.columns,
              pd.MultiIndex):
  df.columns = df.columns.droplevel(1)

custom_style = mpf.make_mpf_style(
    base_mpf_style="charles",
    facecolor="black",
    figcolor="black",
    gridcolor="#333333",
    gridstyle="--",
)

mpf.plot(
    df,
    style=custom_style,
    type="candle",
    volume=True,
    title="AAPL Candlestick Chart",
    mav=(10, 20),
)
