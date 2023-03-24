# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:42:41 2021

@author: Ryan Nevitt (Rabbit)
"""

from alpha_vantage.timeseries import TimeSeries

import matplotlib.pyplot as plt

with open('API_key.txt', "r") as in_file:
       key = in_file.read()


ts = TimeSeries(key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='IBM', interval = '60min', outputsize= 'full' )  #your stock here
data['4. close'].plot()
plt.tight_layout()
plt.title('Intraday Value for IBM')
plt.grid()
plt.gca().invert_xaxis()
plt.show()


