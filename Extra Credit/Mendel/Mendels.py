# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:21:51 2021

@author: Ryan Nevitt (Rabbit)
"""

k = 19                                                    
m = 21                                                        
n = 30                                                       
pop = k + m + n                                               
prob = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*pop*(pop-1))
print(prob)   