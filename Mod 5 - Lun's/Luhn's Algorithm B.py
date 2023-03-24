# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:04:42 2021

@author: Rabbit (Ryan Nevitt)
Milestone Lab: Luhn's Algorithm

### General info
https://en.wikipedia.org/wiki/Luhn_algorithm
https://www.dcode.fr/luhn-algorithm ####used to compare checked numbers numbers

#### operators
https://www.geeksforgeeks.org/enumerate-in-python/
https://blog.tecladocode.com/python-30-day-9-enumerate-zip/
https://www.w3schools.com/python/ref_list_pop.asp 
https://realpython.com/python-or-operator/
https://www.programiz.com/python-programming/if-elif-else
https://stackoverflow.com/questions/12700558/print-without-space-in-python-3
https://www.techbeamers.com/python-convert-list-string/
https://www.guru99.com/reading-and-writing-files-in-python.html
https://stackoverflow.com/questions/17949508/python-read-all-text-file-lines-in-loop ####for loop to read lines

### Videos I watched
https://www.youtube.com/watch?v=p_mO_jpihiw
https://www.youtube.com/watch?v=XGutqiC-REw
https://www.youtube.com/watch?v=5YGoy0SSOY8
"""

#########
#pseudo
#########

# get the cc , ask input ++

# check length ++
    #invalid length error
# check first digits for type of card for (Visa, MC, AMEX) ++
# find out what each card uses to check ++
    #Visa - fd 4, length 13,16
    #Amex- fd 3, 2nd 4,7 length 15
    #MC - fd 5, 2nd 1-5
# use to print card type ++

#slice number ++
    # pop off the end check number ++
    # new string ++
    # reverse string or read backwards ++
    #slice/index the number ++
        ## even's index's are double, odds left alone ++
        # make double digits single digits, add digits or subtract 9 ++
        
#total = sum + check number ++
#check divisible by 10  ++
#print out valid or invalid ++

# print to text file ++

##########


with open('testCCNums.txt') as test:
   for line in test:
        CC = line
        card_org=CC.strip() #learned how important strip was for the input
        card_number = list(card_org) # makes it a list
        
        
        ######################################################
        #Card type and length
        ######################################################
        first_digit = int(card_number[0]) #first card digit
        second_d = int(card_number[1]) #second card digit
        length= int(len(card_number)) #card length
        
        
        
        if first_digit==4 and length==16:
            card = ("VISA:")
        
        elif first_digit==3 and length==15 and (second_d==4 or second_d==7):
            card = ("AMEX:")
        
        elif first_digit==5 and (1<=second_d and second_d <=5) and length==16:
            card ="MC:"
        
        else:
            print("INVALID CARD")
        ###################################################################
        
    
        
        
        
        ##################
        #Luhn's Algorithm
        ##################
        check_digit = card_number.pop()  #new variable that removes the last digit 
        card_number.reverse() #reverse the list  without the check number
        new_digits = [] #empty list for the new doubled numbers
        
        for index, digit in enumerate(card_number): #learned about enumerate for lists, assigns a value to each digit counting up 0,1,2,3...
            if index % 2 ==0:  #checks for even index, the numbers I want to double
                 
                dd= int(digit)*2 # doubles the digits
                if dd > 9:  # checks to see if it's a double digit number
                    dd=dd-9 #makes it a single digit number some references used this instead of adding both digits
                new_digits.append(int(dd)) #new x2 digits and them adds to list
            else:
                new_digits.append(int(digit)) # untouched odd digits and adds them to the list
        ###############
        
        
        
        
        #############
        # printing
        ##############
        total = int(check_digit) + sum(new_digits) #new digits + check digits
        
        if total%10==0:
            p=card_org,"--------",card,"VALID"
            p= ''.join(p) #list back into string, no spaces, sep="" another way to delete spaces
            print(p)
        else:
            p=card_org,"--------INVALID NUMBER"
            p= ''.join(p) 
            print(p)
            
        ###############
        
        
        
        
        ##############
        #Out file
        ##############
        total = int(check_digit) + sum(new_digits) #new digits + check digits
        with open("Mod5_B.txt","a+") as f: # open and append        
            if total%10==0:            
                p=card_org,"--------",card,"VALID\n"
                p= ''.join(p) #list back into string
                f.write(p)
            else:
                p=card_org,"--------INVALID NUMBER\n"
                p= ''.join(p) #list back into string
                f.write(p)    
            if 'str' in line: break  #if string in line, break to next line
        



#########
#checking
#########

# print(new_digits)
# print(check_digit)


### check indexed number
# for index, digit in enumerate( card_number):
#     print (index,digit)
    

    


