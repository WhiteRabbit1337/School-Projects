# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:36:36 2021

@author: Rabbit (Ryan Nevitt)
"""

fibonacci_cache ={}

### compute the nth term ###
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    
    if  n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        value = fibonacci(n-1) + fibonacci(n-2)

###cache the value and return it ###

    fibonacci_cache[n] = value
    return value


for n in range (1,1001):
    print(n, ":" , fibonacci (n))
    