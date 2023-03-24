# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:39:19 2021

@author: Ryan Nevitt (Rabbit)
"""

from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

with open('API_key.txt', "r") as in_file:
       key = in_file.read()

ti = TechIndicators(key, output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.gca().invert_xaxis()
plt.show()