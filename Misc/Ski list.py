# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:15:50 2021

@author: Rabbit(Ryan Nevitt)

Python Crash Course
https://www.programiz.com/python-programming/methods/list/reverse
https://www.programiz.com/python-programming/methods/list/sort
https://www.w3schools.com/python/ref_func_range.asp
"""
#ski brands list
ski_brand = ['Head', 'Volkl', 'Fischer, Salomom', 'Rossingnol','K2'] #Regular list
print(ski_brand)
ski_brand[0] = 'Icelantic' # Replaces first item on list
print(ski_brand)
ski_brand.append ('Line') # adds to end of list
print(ski_brand)
print(ski_brand[-1]) #prints fischer to end of list
ski_brand.insert(2,'Armada') # insert after Volkl
print(ski_brand)
ski_brand.reverse() #reverse list
print(ski_brand)
ski_brand.sort()#sorts aplphabetically
print(ski_brand) 
print() #space

#numbers list
x = range(2,20, 2) # makes a range of numbers from 2 to 18, printing every other number.
for n in x:
  print(n)
  
print()#space

#used Python Crash Course as resource
print(min(x)) #prints the minimun value on list
print(max(x)) #prints the maximum value on the list
print(sum(x)) #sums up all the items on the list
print(len(x)) #Length of the list

print()#space

#used Python Crash Course as resource
cubes  = [] #empty list
for value in range(1,11): #for loop 1 to 10
    cube = value**3 #cubes the next item 
    cubes.append(cube) #adds the next cube to the list
    print(cube) # prints the list of cubes consecutively until it cubes the whole list, adding the next cube on the end and printing it