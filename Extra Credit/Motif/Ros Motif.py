# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 02:34:14 2021

@author: Ryan Nevitt (Rabbit)
https://www.chegg.com/homework-help/questions-and-answers/python-given-two-strings-s-t-t-substring-s-t-contained-contiguous-collection-symbols-s-res-q44507136
"""

s1=input("Enter string: ") #reading the string from user
s2=input("Enter sub_string: ") #reading the sub_string from the user


l1=len(s1) #finding the length of the first string
l2=len(s2) #finding the length of the sec(ond string
print ("sub_string occurences are:")
for i in range(0,l1-l2+1): #from each position checking for the occurence
    if(s1[i:i+l2]==s2):
        print (i+1,) #printing the occurence result