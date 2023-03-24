# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:34:22 2021

@author: Rabbit (Ryan Nevitt)


websites visited:
https://stackoverflow.com/questions/27826214/how-do-i-make-a-space-between-words-when-writing-to-a-text-file-in-python
https://stackoverflow.com/questions/60527271/typeerror-write-takes-exactly-one-argument-2-given-python
https://stackoverflow.com/questions/51477299/python-typeerror-write-takes-exactly-one-argument-2-given/51479522
https://stackoverflow.com/questions/35427814/get-the-number-of-all-keys-in-a-dictionary-of-dictionaries-in-python
https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
https://stackoverflow.com/questions/38401099/how-to-count-one-specific-word-in-python/38401167
"""


from collections import Counter             # import Counter from collections library

with open("rosalind_ini6.txt","r+") as ros: # import text file
    data=ros.read()
    words= data.split()                     # split


count = Counter()                           # counter variable


for word in words:
    count[word] += 1                        # count increment 

with open("Ros_6.txt","w+") as f:
    for k in count.keys():                  # counting the number of keywords in a dictionary
        numb = str(count[k])
        print (k, numb)                     # print the word and and count of that word
        f.write(k + " " + numb + "\n")