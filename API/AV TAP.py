# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:17:19 2021

@author: Ryan Nevitt (Rabbit)
https://towardsdatascience.com/using-python-and-robinhood-to-create-a-simple-buy-low-sell-high-trading-bot-13f94fe93960
https://blog.finxter.com/daily-python-puzzle-maximum-profit-algorithm/
https://thispointer.com/python-how-to-convert-a-list-to-dictionary/
https://www.youtube.com/watch?v=7AMjRbJhsKM
https://www.youtube.com/watch?v=Pw6lrYANjz4
"""

### Pseudo ###
#Import data
    #slice data to year

# how many transactions for max profit

# buy function 
    # buy when next prices is lower 
# sell function 
    # sell when  next price is higher


    

## Allow us to easily work with CSV files
import csv
## Allow us to parse date and time information
from datetime import datetime
## Include plotting libraries
from matplotlib import pyplot as plt

Bank = 10000




filename = 'daily_adjusted_TAP.csv'  #or whatever you named the CSV file when you downloaded it
with open(filename, 'r') as f:
        ## The file is read only
    reader = csv.reader(f)
        ## read the headers row
    header_row = next(reader)
        ## Get dates and prices from this file
    
    
    dates, prices = [], []
    
  
    
    for row in reader:
    
    ## Row 0 contains date information
        current_date = datetime.strptime(row[0], '%m/%d/%Y') 
        dates.append(current_date)
            ## Row 4 contains closing price information
        price = float(row[4])
        prices.append(price)
        
        ### slice to year format ### 
        prices=prices[:257:]  
        dates = dates[:257:]
        ############################
    
    ### Plot prices vs. date ###
    plt.style.use('seaborn') 
    fig, ax = plt.subplots()
    ax.plot(dates, prices, c='red')
    ########################
    
    
    ### Format plot ###
    plt.title("Coors Daily Closing Price (USD)", fontsize=24)  
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("US Dollars", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)   
    plt.show()
    #################




    
### reverse list ###
dates = dates [:-253:-1]
prices = prices [:-253:-1] 
# ######################


# ### dictionary ###
# zipobj = zip(dates, prices)
# dp_dict = dict(zipobj)
# ####################






### max profit for n transactions #####################

n= len(prices) # length of prices

def maxprofit(prices, n):
    if not n:
        return 0
    profits = [[0 for day in prices] for trans in range(n + 1)]
    for trans in range (1, n + 1):
        maxsofar = float("-inf")    # small number to start comparing
        for day in range(1, n):
            maxsofar = max(maxsofar, profits[trans-1][day-1]- prices[day-1])
            profits[trans][day] = max(profits[trans][day-1], maxsofar + prices[day])
        # print(profits[t][day])
          
    return profits[-1][-1] #profits end of list
########################################################




print("Total profit:")
print("$","{:.2f}".format(maxprofit(prices, n)))
Bank = Bank + maxprofit(prices, n)
print()
print("Bank:")
print("$",Bank)

    
### bar chart #################
import matplotlib.pyplot as plt
import datetime
x = sell_list
y = profit_list

ax = plt.subplot(111)
ax.bar(x, y, width=6, edgecolor='black')
ax.xaxis_date()

plt.ylabel('Profit in "$"', fontsize=16)
ax.set_title('2020-2021 Profits for Coors Stock(USD)', fontsize=24)

plt.show()
####################################
