'''
Created on 29 Dec 2017

@author: cmt

SP500 prices are based on yahoo data
Tests if there is correlation in SP500 returns
Much code borrowed from https://machinelearningmastery.com/autoregression-models-time-series-forecasting-python/

'''

print 'Start'
import pandas as pd
import matplotlib.pyplot as plt

#Load data and make timeseries of closing price
series = pd.read_csv('^GSPC.csv', index_col=0)
s = series['Close']
# print(s.head())
# print(s.describe())
# s.plot()
# plt.show()

#generate matrix with price, lagged price and return
from pandas import DataFrame
from pandas import concat
values = DataFrame(s.values)
df = concat([values, values.shift(1), (values-values.shift(1))/values.shift(1)], axis=1)
df.columns = ['t', 't-1', 'return']
# print(df.head())

#Create return timeseries
r = pd.DataFrame(df['return'].values, index=s.index)

#plot lag_plot
from pandas.plotting import lag_plot
lag_plot(r)
plt.show()

#Calculate correlations
v = DataFrame(r.values)
df = concat([v.shift(1), v], axis=1)
df.columns = ['t-1', 't+1']
print(df.corr())

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(r)
plt.show()

print 'Done'

if __name__ == '__main__':
    pass