# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:24:45 2021

@author: Ryan Nevitt (Rabbit)
"""

def ReadNext(sequence):
    for item in sequence:
        yield item.strip()
    yield None 


f = open('rosalind_gc.txt')
items = ReadNext(f)
item = ""

DNAStrings = {}
lastID = ""
tempStr = ""

while True:
	item = items.next()
	if item == None: 
		break
	if item.find('>') != -1:
		lastID = item
		DNAStrings[lastID] = ""
	else:
		DNAStrings[lastID] += item
max_gc_id = ""
percent = 0.0

for x in DNAStrings:
	count = len(DNAStrings[x])
	temp_percent = float(DNAStrings[x].count('G') + DNAStrings[x].count('C'))/float(count)*100.0
	if temp_percent > percent:
		max_gc_id = x
		percent = temp_percent
print (max_gc_id)
print (percent)