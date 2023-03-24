# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:19:55 2021

@author: Ryan Nevitt (Rabbit)
"""

from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
 

with open('API_key.txt', "r") as in_file:
       key = in_file.read()

ti = TechIndicators(key, output_format ='pandas')

data, meta_data = ti.get_bbands( symbol= 'TAP', interval = '60min', time_period = 60)
data.plot()
plt.title("BBands indicator for Coors stock (60days)")
plt.show()



