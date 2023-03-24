# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:33:29 2021

@author: Ryan Nevitt (Rabbit)
"""



###Pseudo###
#import message, key

# encrypt  = (message + key ) % 26
# decrypte = (encrypt - key )  % 26


#encrypt
    #split message to length of key
    #
#decrypt
    #split cypher to the length of the
###ascii###
#A-Z 65- 90
#a-z 97-122
# space 32
###########

### In file ###
with open('Message.txt', "r") as m_file, open('Key.txt','r') as k_file:
    message = m_file.read() 
    key = k_file.read()
#################

key_length = len(key)
message_int = [ord(i) for i in message]
key_int = [ord(i) for i in key]

print(message_int)
print(key_int)

n=0
i=0
ctext = ''
for char in message:
  
    if char.isupper():
        ctext = ctext + chr(((message_int[n] + (key_int[i]-65)-65) % 26) + 65)
        print(message_int[n],key_int[i]-65)
        print(chr(((message_int[n] + key_int[i]-65)-65) % 26 + 65))
        n+=1
        i+=1
    # elif char.islower():
    #    ctext = ctext + chr(((message_int[i] + key_int[n]) - 97) % 26 + 97)
       
       
    else: 
        ctext = ctext + char
        n+=1
        
        
        
    
    
        


    