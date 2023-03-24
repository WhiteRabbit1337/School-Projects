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

Bank = 1000
# Buy_perc = -.5
# Sell_perc = .5



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

n= len(prices) # length of 

# while i<=n:
    
### reverse list ###
dates = dates [::-1]
prices = prices [::-1] 
######################


# ### dictionary ###
# zipobj = zip(dates, prices)
# dp_dict = dict(zipobj)
# ####################





# ### max profit for n transactions #####################
# def maxprofit(prices, n):
#     if not n:
#         return 0
#     profits = [[0 for d in prices] for t in range(n + 1)]
#     for t in range (1, n + 1):
#         maxsofar = float("-inf")
#         for d in range(1, n):
#             maxsofar = max(maxsofar, profits[t-1][d-1]- prices[d-1])
#             profits[t][d] = max(profits[t][d-1], maxsofar + prices[d])
#             # print(maxsofar)
#     return profits[-1][-1]   
# ###############################################   



### max profit for n transactions #####################
def maxprofit(prices,n):
    if not n:
        return 0
    evenprofits = [0 for d in prices]
    oddprofits = [0 for d in prices]
    for t in range (1, n+1):
        maxsofar = float("-inf")
        if t%2 ==1: # odd number of transactions
            currentprofits = oddprofits
            previousprofits = evenprofits
        else:
            currentprofits = evenprofits
            previousprofits = oddprofits
        for d in range (1,n):
            maxsofar = max(maxsofar,previousprofits[d-1] - prices[d-1])
            currentprofits[d] = max(currentprofits[d-1], maxsofar + prices[d])
    return evenprofits[-1] if n%2==0 else oddprofits[-1]
#####################################
print("Total profit:")
print("{:.2f}".format(maxprofit(prices, n)))

    
    
