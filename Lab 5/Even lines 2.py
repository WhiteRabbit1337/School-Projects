# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:57:35 2021

@author: Rabbit (Ryan Nevitt)
lab 5, rosland reading and writing

"""

with open('rosalind_ini5.txt', "r") as in_file, open("even_lines2.txt","w+") as out_file:
       even = list(in_file)[1::2]
       for line in even:
           out_file.write(line)
           print (line)
