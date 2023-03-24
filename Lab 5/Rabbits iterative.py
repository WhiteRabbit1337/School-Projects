# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:40:02 2021

@author: Rabbit (Ryan Nevitt)
"""

    # def rabbits (n,k):
    #     return 1 if (n==1 or n==2)
    #     rabbit_pairs = rabbits(n-2, k) * k + rabbits(n-1, k)
    #     rabbit_pairs
    
        
    # def rabbits(n, k):
    #     fib1 = 1
    #     fib2 = 1
    #     for i in range(2, n):
    #         wabbits = fib1 + k * fib2
    #         fib2 = fib1
    #         fib1 = wabbits
    #     return wabbits
    
n,k = input("What are months (n) and pairs of rabbits (k)? :").split()
n=int(n)
k=int(k)


    #### Fibi for rabbits ###
def rabbits(n, k):
    fn_1, fn_2 = 1, 1
    fn = 1  # Just a place holder in case n is too small
    for _ in range(2, n):
        fn = fn_1 + fn_2*k
        fn_2, fn_1 = fn_1, fn
    return fn
    

### Output ###  
rab=str(rabbits(n,k))

print(rabbits (n,k))
with open("Wabbits.txt","w+") as out_file:  
     out_file.write(rab)
    