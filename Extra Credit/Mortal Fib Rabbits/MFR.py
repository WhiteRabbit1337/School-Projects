# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:05:46 2021

@author: Ryan Nevitt (Rabbit)
https://www.cnblogs.com/think-and-do/p/7274013.html
https://www.bitdegree.org/learn/python-split
"""

# Fn= F(n-1) +F(n-2)
# Fn= F(n-1) +F(n-2) - 1
# Fn= F(n-1) +F(n-2) - F(i - m- 1)

### in file ###################################
with open('rosalind_fibd.txt', 'r') as in_file:
    xy = in_file.read()
    xy = xy.split()
    x = int(xy[0]) 
    y = int(xy[1])
################################################
    

### Fib Funtions #################################
def FibonacciRabbits(n, m):
    F = [0, 1, 1]
    for i in range(3, n + 1):
        if i <= m:
            total = F[i - 1] + F[i - 2]
        elif i == m + 1:
            total = F[i - 1] + F[i - 2] - 1
        else:
            total = F[i - 1] + F[i - 2] - F[i - m - 1]
        F.append(total)
    return (F[n])
########################################################



#### Out File #################################
print (FibonacciRabbits(x,y))
with open("Out_Rabbits.txt", "w") as out_file:
    out_file.write(str(FibonacciRabbits(x,y))) 
#################################################