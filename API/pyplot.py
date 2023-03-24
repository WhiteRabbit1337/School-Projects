# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:13:11 2021

@author: Ryan Nevitt (Rabbit)
"""

import matplotlib.pyplot as pyplot

### initialize x and y data set

x= [0,1,2,3,4,5,6,7,8,9,10]
y= [1,2,4,8,16,32,64,128,256,512,1024]


pyplot.scatter(x,y, label = "powers of two", color = 'r')
pyplot.xlabel('n')
pyplot.ylabel('2 to the n')
pyplot.title("Scatter Plot Example")
pyplot.legend()


### annotate each point
for i in range (0,len(x)):
    pyplot.annotate(xy = [x[i], y[i]], text= y[i])
    
## make the y axis log scale ###

pyplot.show