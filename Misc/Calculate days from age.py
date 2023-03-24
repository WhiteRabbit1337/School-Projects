# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:06:06 2021

@author: Rabbit(Ryan Nevitt)

calculation for age to days 

#googled sum fuction
#https://www.geeksforgeeks.org/sum-function-python/
"""

name = input("What is your name? ")
age = int(input("What is your age? ")) # intput age as interger

#attempting to add months and days to calculation
day= int(input("What day where you born(number)? "))
month= int(input("What is your birthday month (number)? "))
date_month = int(input("What is this years month (number)? "))
date_day = int(input("What is today's date (number)? "))

year = [31,28,31,30,31,30,31,31,30,31,30,31]



day=(year[month+1])-day
month=sum(year[month:])
date_month=sum(year[:date_month])
# print(sum(year))
# print(month)
# print(day)

# going to be off by a day because of leap year, accutrate enough for what I wanted to accomplish
# I think using a some sort of modular funtion % could find out to add or not add a day
days_old = age*365 + age/4+1 + month + day + date_month + date_day

print( f"{name} is {days_old} days old.") #How many days old 

