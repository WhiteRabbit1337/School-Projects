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





### in file ########################################
filename = 'daily_adjusted_TAP.csv'  
with open(filename, 'r') as f:
        ## The file is read only
    reader = csv.reader(f)
        ## read the headers row
    header_row = next(reader)
        ## Get dates and prices from this file
    
    dates, prices = [], []
 #####################################################
  
 
    
### plot graph  ################################################
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
    
    ### Plot prices vs. date ######
    plt.style.use('seaborn') 
    fig, ax = plt.subplots()
    ax.plot(dates, prices, c='red')
    ##############################
    
    
    ### Format plot #######
    plt.title("Coors Daily Closing Price (USD)", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("US Dollars", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)   
    plt.show()
######################################################################



    
### reverse list  ##################
dates = dates [:-253:-1]
prices = prices [:-253:-1] 
# ##################################



###############################
Bank = 10000
n = len(prices)   
profit_list, sell_list = [],[] 
###############################


### clear file ################
file =open("Profit.txt", "r+")
file.truncate(0)
file.close()
################################    


### Max Profit #########################################################
def stockBuySell(prices, n):
     
    # Prices must be given for at least two days
    if (n == 1):
        return
     
    # Traverse through given price array
    i = 0
    profit=0
    while (i < (n - 1)):
         
        # Find Local Minimum
        # the limit is (n-2) 
        # comparing present price to the next price
        while ((i < (n - 1)) and
                (prices[i + 1] <= prices[i])):
            i += 1
         
        # No More solutions
        if (i == n - 1):
            break
         
        # Store the index of minimum
        buy = i
        buyprice = prices[buy]
       
        i += 1
         
        # Find Local Maximum
        # the limit is (n-1) 
        # comparing current price to previous price
        while ((i < n) and (prices[i] >= prices[i - 1])):
            i += 1
            
        # Store the index of maxima
        sell = i - 1
        sellprice = prices[sell]
        selldate =  dates[sell]
        
        ### visualize on what days and how much I'm buying and selling ###
        print("Buy on day:",buy,"\t","Sell on day:",sell,", Date:", selldate) 
        print("$"+str(buyprice),"                ","$"+str(sellprice))
        profit= profit +(sellprice-buyprice)
        print ("Profit:","${:.2f}".format(profit))
        print ()
        
        
        
        
#################################################################
        
        ### lists of profit and date sold ######
        profit_list.append(profit)
        sell_list.append(selldate)
        ###################################
        
        ### Outfile ############################
        with open ("Profit.txt", "a+") as out_file:
            p = ("Buy on day:",str(buy),"         ","Sell on day:",str(sell),", Date: ", str(selldate),"\n")
            p = ''.join(p)
            out_file.write(p)
            q= "$"+str(buyprice),"                ","$"+str(sellprice),"\n"
            q= ''.join(q)
            out_file.write(q)
            r= "Profit:","${:.2f}".format(profit),"\n"
            r=''.join(r)
            out_file.write(r)
            out_file.write("\n")
        ##########################################
    return profit
               
##################################################################





Bank = Bank + stockBuySell(prices, n)

print()
print("Bank:")
print("$"+str(Bank))


Bank= "$"+str(Bank)
with open ("Profit.txt", "a+") as out_file:
    out_file.write("Bank:\n")
    out_file.write(str(Bank))

           

### bar chart #################
import matplotlib.pyplot as plt
import datetime
x = sell_list
y = profit_list

ax = plt.subplot(111)
ax.bar(x, y, width=6, edgecolor='black')
ax.xaxis_date()

plt.ylabel('Profit in US Dollars', fontsize=16)
ax.set_title('2020-2021 Profits for Coors Stock(USD)', fontsize=24)

plt.show()
####################################

    
    
