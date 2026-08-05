import plotly.express as px
import yfinance as yf

df = yf.download("AAPL",
                 start="2026-01-01",
                 end="2026-08-01",
                 progress=False)
df.columns = df.columns.get_level_values(0)

df["simple_rtn"] = df["Close"].pct_change()
df = df[["Close", "simple_rtn"]].dropna()

fig = px.line(
    df,
    y=["Close","simple_rtn"],
    facet_row="variable",
    title="AAPL STOCK RRTN "
)
fig.update_yaxes(matches=None)
fig.show(renderer="browser")
