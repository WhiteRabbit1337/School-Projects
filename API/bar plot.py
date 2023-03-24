# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:42:54 2021

@author: Ryan Nevitt (Rabbit)

https://www.python-graph-gallery.com/12-stacked-barplot-with-matplotlib

"""

# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

 
# y-axis in bold
rc('font', weight='bold')
 
### Values of each group ####
bars1 = [2, 3, 4, 5, 6]
bars2 = [4, 5, 6, 5, 4]
bars3 = [1, 3, 5, 4,3]
 
# Heights of bars1 + bars2
bars = np.add(bars1, bars2).tolist()
 
# The position of the bars on the x-axis
r = [0,1,2,3,4]
 
# Names of group and bar width
names = ['A','B','C','D','E']
barWidth = 1
 

## Pink Bar (bottom)
plt.bar(r, bars1, color='pink', edgecolor='black', width=barWidth)
# Create green bars (middle), on top of the first ones


plt.bar(r, bars2, bottom=bars1, color='green', edgecolor='black', width=barWidth)

# Create blue (top)
plt.bar(r, bars3, bottom=bars, color='blue', edgecolor='black', width=barWidth)
 
# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("Bar Study")
 
# Show graphic
plt.show()