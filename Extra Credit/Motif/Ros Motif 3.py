# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:03:48 2021

@author: Ryan Nevitt (Rabbit)
https://www.chegg.com/homework-help/questions-and-answers/python-given-two-strings-s-t-t-substring-s-t-contained-contiguous-collection-symbols-s-res-q44507136
https://github.com/swetakum/Rosalind/blob/master/FIndingMotifinDNA.py
https://www.geeksforgeeks.org/python-program-to-convert-list-of-integer-to-list-of-string/
https://www.w3schools.com/python/ref_string_find.asp
"""



# While loop to find each instance of tt in ss

### Motif Function #######################
def findMotif(ss,tt):
    
    motifs = []
    n = 0
    while n < len(ss):
        n = ss.find(tt, n)  # string.find(value, start, end)
        if n == -1:
            return motifs
        else:
            motifs.append(n+1)
            n += 1  # change to n += len(sub) to not search overlapping results

    return motifs
##########################################


with open('rosalind_subs.txt', "r") as in_file:
    Motif = in_file.readlines()
    ss = str(Motif[0]).strip()  # mainstring
    tt = str(Motif[1]).strip()  # substring



out = findMotif(ss,tt)
out= [str(i) for i in out]
out2 = " ". join(out)
print(out2)


with open('Motif.txt', "w+") as out_file:
    out_file.write(out2)
