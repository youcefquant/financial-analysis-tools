import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
def get_hurst_ind(ts, max_lag):

    lages=range(2,max_lag)
    tau=[]

    for lag in lages:


        diff=ts[lag:] - ts[:-lag]

        std_d=np.std(diff)

        tau.append(std_d)


    hurst_ex=np.polyfit(np.log(lages),np.log(tau),1)[0]
    return hurst_ex

ticker=yf.Ticker("AAPL")
df=ticker.history(period="1y")

lages_list=[20,
            100,
            200,
            500]

for lag in lages_list:
    hurst_exp=get_hurst_ind(df["Close"].values,lag)

    print(f"Hurst exponent with {lag} lags: {hurst_exp:.4f}")
