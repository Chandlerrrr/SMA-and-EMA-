import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web

# set start and end dates
start = datetime.datetime(2017, 2, 1)
end = datetime.datetime(2020, 2, 1)

aapl_df = web.DataReader(["AAPL"], 'yahoo', start= start, end =end)['Close']
aapl_df.columns = {'Close Price'}
print(aapl_df.head(20))
aapl_df['Close Price'].plot(figsize=(15,8))
plt.grid()
plt.title('Closeprice vs dates')
plt.ylabel('price in $')
plt.show()