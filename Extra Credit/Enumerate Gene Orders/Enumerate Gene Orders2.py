# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:04:06 2021

@author: Ryan Nevitt (Rabbit)
https://www.w3schools.com/python/python_tuples
http://wpressutexas.net/oldcoursewiki/index.php?title=User:Rcardenas:Python2
"""

import itertools
with open('rosalind_perm.txt', 'r') as in_file, open('Out_Gene.txt', "w") as out_file:
    itter = int(in_file.read())
    l = [x for x in range (1,itter+1)]
    l = list(itertools.permutations(l))
    # print (len(l))
    out_file.write(str(len(l)))
    out_file.write("\n")
    for x in l:
        # print(" ". join([str(i) for i in x]))
        out_file.write(" ". join([str(i) for i in x]))
        out_file.write("\n")
        