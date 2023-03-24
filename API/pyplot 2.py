# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:13:11 2021

@author: Ryan Nevitt (Rabbit)
"""

import matplotlib.pyplot as plt


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [10, 45, 20, 38, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men', color= "blue")
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women', color = "pink", edgecolor='white',)

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()



plt.show()