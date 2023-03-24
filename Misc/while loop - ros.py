# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 04:42:57 2021

@author: Rabbit (Ryan Nevitt)
While loop: ini4

"""
### inputs
sum=0
a = int(input("What's the 1st integer?:"))
b = int(input ("What's the 2nd integer?:"))
i=a         #starting interger

### While Loop ####

while (i<=b):       # while the 1st interger is less than the 2nd
    if (i%2==1):    # if its the number is odd add to the sum
        sum+=i 
    i=i+1           # next interger
print (sum)