# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:04:42 2021

@author: Rabbit (Ryan Nevitt)
Milestone Lab: Luhn's Algorithm

### General info
https://en.wikipedia.org/wiki/Luhn_algorithm

#### operators
https://www.geeksforgeeks.org/enumerate-in-python/
https://blog.tecladocode.com/python-30-day-9-enumerate-zip/
https://www.w3schools.com/python/ref_list_pop.asp 
https://realpython.com/python-or-operator/
https://www.programiz.com/python-programming/if-elif-else
https://stackoverflow.com/questions/12700558/print-without-space-in-python-3
https://www.techbeamers.com/python-convert-list-string/
https://www.guru99.com/reading-and-writing-files-in-python.html

### Videos I watched
https://www.youtube.com/watch?v=p_mO_jpihiw
https://www.youtube.com/watch?v=XGutqiC-REw
https://www.youtube.com/watch?v=5YGoy0SSOY8
"""


#pseudo
#########
# get the cc , ask input ++

# check length ++
# check first digits for type of card for (Visa, MC, AMEX) ++
# find out what each card uses to check ++
    #Visa - fd 4, length 13,16
    #MC - fd 5, 2nd 1-5
    #Amex- fd 3, 2nd 4,7
# use to print card type ++

#slice number ++
# pop off the end check number ++
# new string ++
# reverse string ++
#slice/index the number ++
        ## even's index's are double, odds left alone ++
        # make double digits single digits, add digits or subtract 9 ++
        
#total = sum + check number ++
#check divisible by 10  ++
#print out valid or invalid ++

# print to text file

##########


# found strip command to remove space at start or finish of end of number
# now I know why when I enter some online info that it won't take it if it has a space at the end

card_org=input("please enter a CC number:").strip() # original card number

card_number = list(card_org) # makes it a list


############
#Card type
############
first_digit = int(card_number[0]) #first card digit
second_d = int(card_number[1]) #second card digit
length= int(len(card_number)) #card length


 #looked up and and/or commands
 #looked up else if statement "elif"
 #seemed the only way to check for multiple things this
 
#tests for card type

if first_digit==4 and (length==13 or length==16):
    card = ("VISA:")

elif first_digit==3 and length==15 and (second_d==4 or second_d==7):
    card = ("AMEX:")

elif first_digit==5 and (1<=second_d and second_d <=5):
    card ="MC:"

else:
   print("INVALID CARD") # catch to see if passes algorithm but not card type, don't know if it possible, but its not printing wrong numbers anyway


    

###############




##################
#Luhn's Algorithm
#################
check_digit = card_number.pop()  #new variable that removes the last digit 

card_number.reverse() #reverse the list  without the check number

new_digits = [] #empty list for the new doubled numbers

for index, digit in enumerate(card_number): #learned about enumerate for lists, assigns a value to each digit 0,1,2.. 
    if index % 2 ==0:  #checks for even index, the ones I want to double
         
        dd= int(digit)*2 # doubles the digits
        if dd > 9:  # checks to see if it's a double digit number
            dd=dd-9 #makes it a single digit number some references used this instead of adding both digits
    
        new_digits.append(int(dd)) #new x2 digits and turn then back into a numbers
    else:
        
        new_digits.append(int(digit))
#############




##############
#printing
###############
total = int(check_digit) + sum(new_digits) #new digits plus check digits

if total%10==0:
    # print(card_org,"--------",card,"VALID",sep="")  #used sep="" to remove spaces ### didnt' need
    p=''.join(card_org,"--------",card,"VALID")

    print(p)
else:
    p=card_org,"--------INVALID NUMBER"
    p= ''.join(p) #list back into string
    print(p)
    
################




#############
#files to note
##############
f=open("Mod5.txt", "a+") # open file


if total%10==0:

    p=card_org,"--------",card,"VALID/n"
    p= ''.join(p) #list back into string
    f.write(p)
else:
    p=card_org,"--------INVALID NUMBER\n"
    p= ''.join(p) #list back into string
    f.write(p)
    
f.close() # close files



#######
#checking
########

# print(new_digits)
# print(check_digit)


### checks indexed number
# for index, digit in enumerate( card_number):
#     print (index,digit)
    


