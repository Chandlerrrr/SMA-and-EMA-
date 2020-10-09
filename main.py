import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl

tickersymbol = 'AAPL'
# MDB for mongodb , MSFT for microsoft

tickerdata = yf.Ticker(tickersymbol)

tickerdf = tickerdata.history(period='1d', start='2010-1-1', end='2017-10-09')

# print(tickerdata.info)
# print(tickerdata.calendar)
# print(tickerdata.recommendations)

print(tickerdf.to_string())
close_px = tickerdf['Volume']
mavg = close_px.rolling(window=100).mean()
mpl.rc('figure', figsize=(8, 7))

style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.title('Apple stock price with Volume')
plt.show()
plt.legend()

rets = close_px / close_px.shift(1) - 1
rets.plot(label='Expected return')
plt.title('expected return')
plt.show()

