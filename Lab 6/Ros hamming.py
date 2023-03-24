# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:54:34 2021

@author: Ryan Nevitt (Rabbit)
https://www.geeksforgeeks.org/hamming-distance-two-strings/
https://github.com/mtarbit/Rosalind-Problems/blob/master/e005-hamm.py
"""


### In file ########################################
with open('rosalind_hamm.txt', "r") as in_file:
    lines = in_file.readlines()     
    s= lines[0]
    t= lines[1]
####################################################


### Hamming distance #############
def hamming(s,t):
    length = 0
    for i in range(0, len(s)):
        if s[i]!= t[i]:
            length+=1
    return length
#################################


### Out file ##################################
print(hamming(s,t))
with open('Ros_hamm_out.txt', "w+") as out_file:
    out_file.write(str(hamming(s,t)))
###############################################