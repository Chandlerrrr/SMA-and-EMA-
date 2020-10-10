import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web

# sets the start and end dates for stocks
start = datetime.datetime(2017, 2, 1)
end = datetime.datetime(2020, 10, 1)

# extracts the daily closing price data
aapl_df = web.DataReader(["AAPL"], 'yahoo', start=start, end=end)['Close']
aapl_df.columns = {'Close Price'}

aapl_df['20_EMA'] = aapl_df['Close Price'].ewm(span=20, adjust=False).mean()
aapl_df['50_EMA'] = aapl_df['Close Price'].ewm(span=50, adjust=False).mean()

# create a new column 'Signal' such that if 20-day EMA is greater   # than 50-day EMA then set Signal as 1 else 0
aapl_df['Signal'] = 0.0
aapl_df['Signal'] = np.where(aapl_df['20_EMA'] > aapl_df['50_EMA'], 1.0, 0.0)

# create a new column 'Position' which is a day-to-day difference of # the 'Signal' column
aapl_df["Position"] = aapl_df['Signal'].diff()

plt.figure(figsize=(20, 10))
# plot close price, short-term and long-term moving averages
aapl_df['Close Price'].plot(color='k', lw=1, label='Close Price')
aapl_df['20_EMA'].plot(color='b', lw=1, label='20-day EMA')
aapl_df['50_EMA'].plot(color='g', lw=1, label='50-day EMA')
# plot ‘buy’ signals
plt.plot(aapl_df[aapl_df['Position'] == 1].index,
         aapl_df['20_EMA'][aapl_df['Position'] == 1],
         '^', markersize=10, color='g', label='buy')
# plot ‘sell’ signals
plt.plot(aapl_df[aapl_df['Position'] == -1].index,
         aapl_df['20_EMA'][aapl_df['Position'] == -1],
         'v', markersize=10, color='r', label='sell')
plt.ylabel('Price in Rupees', fontsize=15)
plt.xlabel('Date', fontsize=15)
plt.title('AAPL - EMA CROSSOVER', fontsize=20)
plt.legend()
plt.grid()
plt.show()
