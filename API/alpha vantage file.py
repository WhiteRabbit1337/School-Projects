# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:03:11 2021

@author: Ryan Nevitt (Rabbit)
"""

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd


with open('API_key.txt', "r") as in_file:
       key = in_file.read()

ts = TimeSeries(key, output_format='pandas')

data, meta_data = ts.get_intraday(symbol='TAP', interval='5min', outputsize= 'full')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
     print(data.describe(), file=open('TAP.txt', 'w'))