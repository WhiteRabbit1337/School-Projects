# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:29:30 2021

@author: Ryan Nevitt (Rabbit)
https://github.com/timothymahajan/Project-Rosalind-Bioinformatics-Stronghold/blob/master/013_IEV/IEV.py
"""

with open("rosalind_iev.txt", "r") as in_file:
    f = in_file.readline()
    b = f.split(" ")
    bint = []
    for i in range (0, len(b)):
        bint.append(int(b[i]))
    
    def Offspring (a):
        sum = (a[0] * 1 + a[1] * 1 + a[2] * 1 + a[3] *0.75 + a[4] *0.5 + a[5] * 0) * 2
        return sum
    
print(Offspring(bint))

with open ("out_offspring.txt", "w") as out_file:
    out_file.write(str(Offspring(bint)))