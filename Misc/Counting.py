# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 08:12:39 2021

@author: Rabbit (Ryan Nevitt)

https://www.w3schools.com/python/ref_list_count.asp  #counting, this method was the easiest to use
https://www.programiz.com/python-programming/methods/list/count
"""

#string given

s='GAATTAGTAGCCTATATCTGGTAAGGGCCGGTCCTAATCTCGGACTCCCCCCCCAAAGTTTCTTTCTGGTGCGCCGGGGTAAAACCGTCACCTTTAGCACGAGACAGTTAAAATCGTCGAACTTATGTTGAAGTCCGATGCTACCGTGGCATACGGAAACTACAGACCCCCGCACCTGAGTGTTGTACCCCGGGCGTAGTCTGGTCCCGGCCAATACCTCTTAGATGCCGGCGGGTGTCTTGGGTATCTCTAAAGTTAGTAGCGTCATTTTGGATGAACCAAGTTTACCATTGAGAAACAACATTTAAATAGCCAACTTGCTGCCCTAGGCTAATCGGGAGCAAAAGTGTGCGGATCTCACTCGTAATCCACTTTCGGGGCTATTTATTGGGTCGGCTCACCCCTGGGGCAGGTAAGAGCGGCACCGTGAAGGGTCACTATATAAAGTGTCACGAGGCACATAATAATCTTACGATTGTTCCAGTTTAGCTTTGTCGTAGCGCGGTATAGGTACTCTGCGGTCGTGTTGTTGACGAACAAAAAACGCCTCCACACCGAACAATGACTTCCTTAACACAATAGCCCGCCCGTTCTGGGATGGCCGCTAGGCAAGATATATCTCGCAAGTATTAAAGAAGCCAGAGCCTTAGCAAAAAAAACGCAGTGGCCCTACGGAGCATATGTGAACATTAGGGCCGCCGGTAGAATGTACCCTAATTCAAAACTACGAGCTCCAACAGCAGGTCGCGGGTAGTTTTCACCTCTACACACCGACGGGGACGGATGGCTTTCCTTCGCATCCTCGGCCAAGAGGTTAGTTGTATTACTGGTGACTTCAACCGCTCACATTGTTAGATACTGGTCAATCGCACAATACGTGCGTCACTTAGGGCTTTACATTAAAATCGTCCACTCTTACGCTGCTGACTGCTTCAGAAAATATTGTCGGGACCGTAGA'

# Counting each string
A = s.count('A')
C = s.count('C')
G = s.count('G')
T = s.count('T')
print (A,C,G,T)