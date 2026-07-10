#Scraping data from Yahoo Finance
import yfinance as yf
import numpy as np
import pandas as pd
import pandas_datareader as pdr
stock=yf.download("AAPL",
               start="2025-01-01",
               end="2026-01-01",
               auto_adjust=True)
stock.head()
#Pulling news data from the Feed website
cpi=pdr.get_data_fred("CPIAUCSL",
                      start="2026-01-01"
                      ,end="2026-06-13")
cpi.head()
#Pulling data from Nasdaq Data Link
import pandas as pd
import nasdaqdatalink
nasdaqdatalink.ApiConfig.api_key = "YOUR_NASDAQ_API_KEY"
df = nasdaqdatalink.get(dataset="WIKI/AAPL",
 start_date="2011-01-01",
 end_date="2021-12-31")
df.head()
