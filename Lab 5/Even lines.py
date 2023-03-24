# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:23:10 2021

@author: Rabbit (Ryan Nevitt)
lab 5, rosland reading and writing

"""

with open('rosalind_ini5.txt', "r") as in_file, open("even_lines.txt","w+") as out_file:
        i = 1
        for line in in_file.readlines():
            if i%2 == 0:
                out_file.write(line)
                print(line)
            i+=1
        

 

        
  