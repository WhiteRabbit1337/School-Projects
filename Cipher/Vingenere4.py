# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:33:29 2021

@author: Ryan Nevitt (Rabbit)
Vingenre Cypher

websites:
https://www.geeksforgeeks.org/vigenere-cipher/
https://geektechstuff.com/2020/01/03/vigenere-cipher-python/
https://www.geeksforgeeks.org/python-numbers-choice-function/a
"""

### Pseudo ###
#ask for encrypt or decrypt
#import message, key

#encrypt
    # split message to length of key
    # encrypt  = (message + key ) % 26
#decrypt
    # split cypher to the length of the key
    # decrypt = (encrypt - key )  % 26
#output    
    
### ascii ###
# A-Z 65-90
# a-z 97-122
# space 32
#############


### Encrypt or Decrypt #################################################
choice = input("Enter 1 for Encryption.\nEnter 2 for Decryption.\n>>> ")
choice = int(choice)
########################################################################
print()

### Encrypt ###

if choice == 1:
    ### User Input ##################################
    message = input("What is the Secret Message?: ")
    keyword = input("What is the key phrase?: ")
    #################################################
    
    # ### In file #############################################################
    # with open('Message.txt', "r") as m_file, open('Key.txt','r') as k_file:
    #     message = m_file.read() 
    #     keyword = k_file.read()
    # #########################################################################
    
    
    #################################################
    # make key same length as message for encrypt key
    #################################################
    def GenerateKey(message, key):
    	key = list(key)
    	if len(message) == len(key):
    		return(key)
    	else:
    		for i in range(len(message) - len(key)):
    			key.append(key[i % len(key)])
    	return("" . join(key))
    key = GenerateKey(message, keyword)
    ################################################
    
    
    ### Encrpyt ##################################################################
    message_int = [ord(i) for i in message]
    key_int = [ord(i) for i in key]
    n=0
    i=0
    ctext = ''
    for char in message:  
        
        if char.isupper():
            if 65<=key_int[i]<=90:
                ctext = ctext + chr(((message_int[n] + (key_int[i]-65)-65) % 26) + 65)
                # print(message_int[n],key_int[i]-65)
                # print(chr(message_int[n]),chr(((message_int[n] + key_int[i]-65)-65) % 26 + 65))    
            else:
                ctext = ctext + chr(((message_int[n] + (key_int[i]-97)-65) % 26) + 65)
                # print(message_int[n],key_int[i]-97)
                # print(chr(((message_int[n] + key_int[i]-97)-65) % 26 + 97))  
            n+=1
            i+=1 
        elif char.islower():
            if 97<=key_int[i]<=122:
                ctext = ctext + chr(((message_int[n] + (key_int[i]-97)-97) % 26)+97)
                # print(message_int[n],key_int[i],key_int[i]-65,(((key_int[i]-97)-65) % 26) + 97)
                # print(chr(message_int[n]),chr(((message_int[n] + key_int[i]-97)-65) % 26 + 97))
            else:
                ctext = ctext + chr(((message_int[n] + (key_int[i]-65)-97) % 26) + 97)      
            n+=1
            i+=1
        else: 
            ctext = ctext + char
            n+=1
           
    ###############################################################################
    
    ### Out file ###################################
    print("Original:", message)
    print("Cipher:  ", ctext)
    with open('Cipher_text.txt', "w+") as out_file:
             out_file.write(ctext)
    ################################################





### Decrypt ###

elif choice == 2:
    ### User Input ##################################
    cipher = input("What is the Cipher?: ")
    keyword = input("What is the key phrase?: ")
    #################################################
    
    
    # ### In file ############################################################
    # with open('Cipher.txt', "r") as c_file, open('Key.txt','r') as k_file:
    #     cipher = c_file.read() 
    #     keyword = k_file.read()
    # #########################################################################
     
    
    #################################################
    # make key same length as Cypher for decrpyt key
    #################################################
    def GenerateKey(cipher, key):
    	key = list(key)
    	if len(cipher) == len(key):
    		return(key)
    	else:
    		for i in range(len(cipher) - len(key)):
    			key.append(key[i % len(key)])
    	return("" . join(key))
    key = GenerateKey(cipher, keyword)
    ##################################3#############
    
    ### Decrypt Code ##########################################################
    cipher_int = [ord(i) for i in cipher]
    key_int = [ord(i) for i in key]
    n=0
    i=0
    ctext = ''
    for char in cipher:
        if char.isupper():
            if 65<=key_int[i]<=90:
                ctext = ctext + chr(((cipher_int[n] - (key_int[i]-65)-65) % 26) + 65)
            else:
                ctext = ctext + chr(((cipher_int[n] - (key_int[i]-97)-65) % 26) + 65)
            # print(message_int[n],key_int[i]-65)
            # print(chr(((message_int[n] - key_int[i]-65)-65) % 26 + 65))
            n+=1
            i+=1
        elif char.islower():
            if 97<=key_int[i]<=122:
                ctext = ctext + chr(((cipher_int[n] - (key_int[i]-97)-97) % 26) + 97)
            else:
                ctext = ctext + chr(((cipher_int[n] - (key_int[i]-65)-97) % 26) + 97)
            # print(message_int[n],key_int[i]-97)
            # print(chr(((message_int[n] - key_int[i]-97)-97) % 26 + 97))
            n+=1
            i+=1
        else: 
            ctext = ctext + char
            n+=1
    ###############################################################################
    
    
    ### Out file ###############################
    print("Cipher: ", cipher)
    print("Decoded:", ctext)
    with open('Decoded.txt', "w+") as out_file:
             out_file.write(ctext)
    #############################################
    



# print(message_int)
# print(key_int)
