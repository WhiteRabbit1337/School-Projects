# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 05:42:18 2021

@author: Rabbit (Ryan Nevitt)


### sources ###
https://www.guru99.com/reading-and-writing-files-in-python.html
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""


# opens file Rabbit, if already made
# blank the first time, will have same text if run subsiquent times
f=open("Rabbit.txt", "r")
print(f.read())

# writes new
f=open("Rabbit.txt", "w")
f.write("This is the beginning\n")

#still writes new with step counter
for i in range(3):
    f.write ("This is the middle %d \n" % (i+1))


# appends on the end
f=open("Rabbit.txt", "a")
f.write("This is the end!!\n")
f.close() #closes here


# reads middle line
with open("Rabbit.txt","r") as f:
    f1=f.readlines()
    print(f1[2])


print(f.closed)