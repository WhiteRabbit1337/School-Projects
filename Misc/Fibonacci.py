# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:53:00 2021

@author: Rabbit (Ryan Nevitt)

https://www.w3schools.com/python/python_while_loops.asp
https://realpython.com/python-while-loop/
https://www.geeksforgeeks.org/python-while-loops/
https://www.chegg.com/homework-help/questions-and-answers/following-recurrence-relation-defines-fibonacci-numbers-fn-f0-1-f1-1-fn-fn-1-fn-2-n-2-writ-q55551597
https://youtu.be/Qk0zUZW-U_M
"""

### easy way of storing cache###
from functools import lru_cache
@lru_cache(maxsize = 1000)


   ### Fibonacci Sequence, function ###
def fibonacci(n):
    if  n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)


i= input("How many Fibonacci numbers? : ")
i= int(i)

### check that the input is a positive integer ###
if type (i) != int: # != not equal to integer                                    
    raise TypeError("input must a posative integer")
if i<1:
    raise TypeError("input must a posative integer")
    
        
### Printing ###
for n in range (1,i+1):
    print(n, ":" , fibonacci (n))


with open("Fibonacci.txt","w+") as f:
    for n in range (1,i+1):
        p = [str(n), ':'," ", str(fibonacci(n)),"\n"]
        for line in p:
            f.write(line)
        
  




# #initial variables
# F0 = 1 # First Fiponacci number
# F1 = 1 # Second Fiponacci number
# i=0 #step counter
# print("The first 12 Fibonacci numbers:")

# #### Fibonacci series ###
# print(F0)                   # prints the First Fiponacci number
# print(F1)                   # prints the 2nd Fiponacci number


# while i<10:                 # while loops the next 10 numbers in the fibonacci sequence until 10 loops
#     temp=F1                 #store the temporary value for the next number(F1) for the calculation
#     F1=F0+F1                #calculation for the next number, the previous 2 numbers add up to the next number in
#                             # the sequence, seemed easier than using n terms
                            
#     print(F1)               #prints the newly calulated F1
#     F0=temp                 #sets F0 as the previous F1 before the new calculation for the next loop
#     i=i+1                   # step counter for the next loop until i is no longer less than 10