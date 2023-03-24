# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:03:28 2021

@author: Ryan Nevitt (Rabbit)
"""

import itertools
with open('test.txt', 'r') as in_file:
    itter = int(in_file.read())
    l = [x for x in range (1,itter+1)]
    l = list(itertools.permutations(l))
    print (len(l))
    for x in l:
    	
    	out = [str(i) for i in x]
    	print( " ". join(out))
        
# with open('Out_Gene.txt', "w+") as out_file:
    # out_file.write()
        