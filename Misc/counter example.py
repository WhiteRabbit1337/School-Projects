# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 01:43:32 2021

@author: Rabbit (Ryan Nevitt)
"""

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
