import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web

# set start and end dates
start = datetime.datetime(2017, 2, 1)
end = datetime.datetime(2020, 10, 1)

aapl_df = web.DataReader(["AAPL"], 'yahoo', start=start, end=end)['Close']
aapl_df.columns = {'Close Price'}
aapl_df['Close Price'].plot(figsize=(15, 8))
aapl_df['20_SMA'] = aapl_df['Close Price'].rolling(window=20, min_periods=1).mean()
aapl_df['50_SMA'] = aapl_df['Close Price'].rolling(window=50, min_periods=1).mean()
aapl_df['Signal'] = 0.0
aapl_df['Signal'] = np.where(aapl_df['20_SMA'] > aapl_df['50_SMA'], 1.0, 0.0)
aapl_df["Position"] = aapl_df['Signal'].diff()
print(aapl_df.head())
plt.grid()
plt.title('Closeprice vs dates')
plt.ylabel('price in $')
plt.show()

plt.figure(figsize=(20, 10))
# plot close price, short-term and long-term moving averages
aapl_df['Close Price'].plot(color='k', label='Close Price')
aapl_df['20_SMA'].plot(color='b', label='20-day SMA')
aapl_df['50_SMA'].plot(color='g', label='50-day SMA')
# plot ‘buy’ signals
plt.plot(aapl_df[aapl_df['Position'] == 1].index,
         aapl_df['20_SMA'][aapl_df['Position'] == 1],
         '^', markersize=10, color='g', label='buy')
# plot ‘sell’ signals
plt.plot(aapl_df[aapl_df['Position'] == -1].index,
         aapl_df['20_SMA'][aapl_df['Position'] == -1],
         '^', markersize=10, color='r', label='sell')
plt.ylabel('Price in Rupees', fontsize=15)
plt.xlabel('Date', fontsize=15)
plt.title('AAPL', fontsize=20)
plt.legend()
plt.grid()
plt.show()
