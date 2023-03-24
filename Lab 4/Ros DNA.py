# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 02:43:28 2021

@author: Rabbit (Ryan Nevitt)
Ros DNA lab

https://github.com/ogencoglu/rosalind/blob/master/bioinformatics_textbook_track/1B.py
https://www.tutorialspoint.com/python-maketrans-and-translate-functions
https://stackoverflow.com/questions/509211/understanding-slice-notation

"""
# 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of "GTCA" is "TGAC").


with open("rosalind_revc.txt", "r") as tf:
    DNA = tf.readlines()[0].strip()         #readlines first item and strip
    

### Find and replace complement ###
    DNA = DNA.replace('A','t')
    DNA = DNA.replace('T','a')
    DNA = DNA.replace('G','c')
    DNA = DNA.replace('C','g')
    rev_com = DNA.upper()[::-1]             # make string uppercase and read in reverse by 1 letter
    
    
        
###### Print ########
print(rev_com)
with open("Ros_DNA.txt","w+") as f:
        f.write(rev_com)
        
    
        
        

