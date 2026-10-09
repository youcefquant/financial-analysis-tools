import numpy as np
import yfinance as yf
import seaborn as sns
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib.pyplot as plt

df=yf.download("AAPL",
               start="2025-01-01",
               end="2026-01-01",
               progress=True,
               multi_level_index=False)

df=df[["Close"]].rename(columns={"Close":"price"})
df["rtn_log"]=np.log(df["price"]/ df["price"].shift(1))
df.dropna()

r_range=np.linspace(min(df["rtn_log"]),
                    max(df["rtn_log"]),
                    num=100)
mun=df["rtn_log"].mean()
sigma=df["rtn_log"].std()
norm_pdf=scs.norm.pdf(r_range,
                      loc=mun,
                      scale=sigma)
fig ,ax=plt.subplots(1, 2, figsize=(16, 8))
sns.histplot(df["rtn_log"]
             ,stat="density",
             ax=ax[0],
             color="skyblue",
             alpha=0.6)
ax[0].plot(r_range,
              norm_pdf,
              "g-",
              lw=2)
ax[0].set_title("Distribution of S&P 500 returns", fontsize=20)
sm.qqplot(df["rtn_log"].values,
          line="s"
          ,ax=ax[1] )
ax[1].set_title("qq piles", fontsize=20)

#To calculate and plot returns
(
    df["rtn_log"]
    .plot(title="S&P 500 returns",
          figsize=(16, 8),
          color="skyblue")
)
#To find out if the previous days are related to the upcoming days and have an effect on them
import matplotlib.pyplot as plt

import statsmodels.tsa.api as smt
n_lages=50
signf=0.05
clean_data=df["rtn_log"].dropna().values

asf = smt.graphics.plot_acf(clean_data,
                            lags=n_lages,
                            alpha=signf)
plt.show()
