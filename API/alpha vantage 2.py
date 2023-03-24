# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:40:20 2021

@author: Ryan Nevitt (Rabbit)
"""

from alpha_vantage.timeseries import TimeSeries

import matplotlib.pyplot as plt

with open('API_key.txt', "r") as in_file:
       key = in_file.read()

ts = TimeSeries(key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')

## The following line flips the x axis to read left to right
plt.gca().invert_xaxis()
plt.show()