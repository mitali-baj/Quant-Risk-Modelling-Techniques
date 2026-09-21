import yfinance as yf
import pandas as pd
import numpy as np

""" fetch from yahoo finance """
reliance = yf.download("RELIANCE.NS","2025-01-01","2026-01-01")
adani = yf.download("ADANIENT.NS","2025-01-01","2026-01-01")
lt = yf.download("LT.NS","2025-01-01","2026-01-01")

""" Create Prices dataframe """
data = pd.DataFrame(reliance["Close"])
data['ADANIENT.NS'] = adani["Close"]
data['LT.NS'] = lt["Close"]

""" Generate Returns dataframe """
returns = (data / data.shift(1)) -1
returns.drop(returns.index[0],inplace=True)

""" Portfolio Initialization """
portfolio = pd.Series({"RELIANCE.NS":50000,"ADANIENT.NS":50000,"LT.NS":100000})

""" PnL dataframe """
pnl = returns * portfolio
pnl['Portfolio_pnl'] = pnl.sum(axis=1)