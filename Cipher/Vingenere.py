# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:12:41 2021

@author: Ryan Nevitt (Rabbit)
Vingenere Ciphor: Milestone Lab
"""

###Pseudo###
#import message, key





#encrypt
    #split message to length of key
    # encrypt  = (message + key ) % 26
#decrypt
    #split cypher to the length of the key
    # decrypte = (encrypt - key )  % 26
###ascii###
#A-Z 65- 90
#a-z 97-122
# space 32
###########


### In file ###
with open('Message.txt', "r") as m_file, open('Key.txt','r') as k_file:
    message = m_file.read() 
#################


### Encryption ###

def encrypt(message, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    message_int = [ord(i) for i in message]
    key = k_file.read()
    cipher = ''
    for i in range(len(message_int)):
        value = (message_int[i] + key_as_int[i % key_length]) % 26
        
        cipher += chr(value + 65)
    return cipher


def decrypt(cipher, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    cipher_int = [ord(i) for i in cipher]
    message = ''
    for i in range(len(cipher_int)):
        value = (cipher_int[i] - key_as_int[i % key_length]) % 26
        message += chr(value + 65)
    return message


print (encrypt(message, key))

