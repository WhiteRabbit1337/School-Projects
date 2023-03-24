# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:28:48 2021

@author: Rabbit (Ryan Nevitt)
"""
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    ##check that the input is a positive integer##
    if type (n) != int:
        raise TypeError("n must a posative integer")
    if n<1:
        raise TypeError("n must a posative integer")
    
    #compute the nth term
    if  n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range (1,1001):
    print(n, ":" , fibonacci (n))
    