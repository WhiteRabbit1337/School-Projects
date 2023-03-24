# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 07:15:20 2021

@author: Rabbit (Ryan Nevitt)

https://stackoverflow.com/questions/16129650/what-does-x-2-0-mean
"""

a=4485
b=9119


result = 0
for i in range(a,b+1):
  if i%2 == 1:
    result += i
print (result)