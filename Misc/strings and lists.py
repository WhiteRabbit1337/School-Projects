# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:09:28 2021

@author: Rabbit (Ryan Nevitt)
"""
# random string
s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."

# number's given
a= 22
b= 27
c= 97
d= 102

# The slice of this string from indices a through b and c through d (with space in between), inclusively.
# In other words, we should include elements s[b] and s[d] in our slice.
print (s[a:b+1] + " " + s[c:d+1]) #a to b+1 to so it returned humpty, same for c to d for dumpty, added quotes for space
