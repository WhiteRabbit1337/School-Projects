# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:47:32 2021

@author: Ryan Nevitt (Rabbit)
"""

## Allow us to easily work with CSV files

import csv

## Allow us to parse date and time information

from datetime import datetime

## Include plotting libraries

from matplotlib import pyplot as plt

filename = 'intraday_5min_IBM.csv'  #or whatever you named the CSV file when you downloaded it

f = open(filename, 'r')

    ## The file is read only

reader = csv.reader(f)

    ## read the headers row

header_row = next(reader)

    ## Get dates and prices from this file

dates, prices = [], []

for row in reader:

## Row 0 contains date information

    current_date = datetime.strptime(row[0], '%m/%d/%Y %H:%M')  #this is year, month, date, order may be wrong? check your data

    dates.append(current_date)

        ## Row 4 contains closing price information

    price = float(row[4])

    prices.append(price)

## Plot prices vs. date

plt.style.use('seaborn') ## one of many plotting styles to choose from

fig, ax = plt.subplots()

ax.plot(dates, prices, c='red')

## Format plot.

plt.title("IBM Daily Closing Price (USD)", fontsize=24)  #change to your Stock's name

plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel("US Dollars", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

f.close()

