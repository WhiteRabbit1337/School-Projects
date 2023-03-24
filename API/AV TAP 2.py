# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:17:19 2021

@author: Ryan Nevitt (Rabbit)
https://towardsdatascience.com/using-python-and-robinhood-to-create-a-simple-buy-low-sell-high-trading-bot-13f94fe93960
https://blog.finxter.com/daily-python-puzzle-maximum-profit-algorithm/
https://thispointer.com/python-how-to-convert-a-list-to-dictionary/
https://www.youtube.com/watch?v=7AMjRbJhsKM
https://www.youtube.com/watch?v=
https://www.geeksforgeeks.org/stock-buy-sell/
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
        prices=prices[:254:]  
        dates = dates[:254:]
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
dates = dates [::-1]
prices = prices [::-1] 
# ######################


# ### dictionary ###
# zipobj = zip(dates, prices)
# dp_dict = dict(zipobj)
# ####################






def maxProfit(price, start, end):
 
    # If the stocks can't be bought
    if (end <= start):
        return 0;
 
    # Initialise the profit
    profit = 0;
 
    # The day at which the stock
    # must be bought
    for i in range(start, end, 1):
 
        # The day at which the
        # stock must be sold
        for j in range(i+1, end+1):
 
            # If byuing the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
                 
                # Update the current profit
                curr_profit = price[j] - price[i] +\
                            maxProfit(price, start, i - 1)+ \
                            maxProfit(price, j + 1, end);
 
                # Update the maximum profit so far
                profit = max(profit, curr_profit);
                # print(profit)
 
    return profit;
 
# Driver code
if __name__ == '__main__':
    price = prices;
    n = len(price);
 
    print(maxProfit(price, 0, n - 1));



print("Total profit:")
print("$","{:.2f}".format(maxProfit(prices, n)))
Bank = Bank + maxProfit(prices, n)
print()
print("Bank:")
print("$",Bank)

    
    
