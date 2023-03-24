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
        prices=prices[:253:]  
        dates = dates[:253:]
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







def stockBuySell(prices, n):
     
    # Prices must be given for at least two days
    if (n == 1):
        return
     
    # Traverse through given price array
    i = 0
    profit=0
    while (i < (n - 1)):
         
        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
                (prices[i + 1] <= prices[i])):
            i += 1
         
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
         
        # Store the index of minima
        buy = i
        buyprice = prices[buy]
       
        i += 1
         
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (prices[i] >= prices[i - 1])):
            i += 1
            
        # Store the index of maxima
        sell = i - 1
        sellprice = prices[i-1]
       
        print("Buy on day: ",buy,"\t","Sell on day: ",sell) #helps visual on what days and how much i'm buying and selling
        print(buyprice,"                ",sellprice)
        profit=(sellprice-buyprice)
        print (profit)
n = len(prices)
# Fucntion call
stockBuySell(prices, n)
##################################################################


# print("Total profit:")
# print("$","{:.2f}".format(maxProfit(prices, n)))
# Bank = Bank + maxProfit(prices, n)
# print()
# print("Bank:")
# print("$",Bank)

    
    
