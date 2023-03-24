# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:44:16 2021

@author: Ryan Nevitt (Rabbit)
"""

import csv

filename = 'daily_adjusted_TAP.csv'

f = open(filename, 'r')

reader = csv.reader(f)

# read the headers row

header_row = next(reader)

for index, column_header in enumerate(header_row):
     print(index, column_header)

f.close()