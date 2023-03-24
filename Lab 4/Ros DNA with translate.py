# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 03:51:17 2021

@author: Rabbit (Ryan Nevitt)
Ros DNA lab

https://github.com/ogencoglu/rosalind/blob/master/bioinformatics_textbook_track/1B.py
https://www.tutorialspoint.com/python-maketrans-and-translate-functions
https://www.youtube.com/watch?v=ZCoHZNg3RPk
https://stackoverflow.com/questions/509211/understanding-slice-notation
"""



with open("rosalind_revc.txt", "r") as tf:
    DNA = tf.readlines()[0].strip()     #readlines first item and strip
    reg = 'ACGT'                        #regular string
    com = 'TGCA'                        #compliment
    
    dict = str.maketrans(reg,com)       # dictionary for for the compliments, repsented in ordinals
     
    rev_com = DNA[::-1].translate(dict) # translate and reverse string

 

###### Print ########
print(rev_com)
with open("Ros_DNA2.txt","w+") as f:
        f.write(rev_com)