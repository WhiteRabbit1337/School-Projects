"""
Created on Tue Mar 30 18:31:29 2021

@author: Rabbit (Ryan Nevitt)

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




### Encryt ###################################################################
if choice == 1:
    # ### User Input ##################################
    # message = input("What is the Secret Message?: ")
    # keyword = input("What is the key phrase?: ")
    # ##################################################
    
    ### In file ##############################
    with open('Message.txt', "r") as in_file:
            file = in_file.read()
            # int_list = file.split()
            message = file 
    ###########################################    
   
    s = int(input("Enter Shift: "))
    ctext = ''
    for char in message:
        if char.isupper():
            ctext = ctext + chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
           ctext = ctext + chr((ord(char) + s - 97) % 26 + 97)
        else: 
            ctext = ctext + char
################################################################################   
 

### Decrypt ####################################################################
elif choice == 2:
    # ### User Input ##################################
    # cipher = input("What is the Cipher?: ")
    # keyword = input("What is the key phrase?: ")
    # #################################################
    
    
    ### In file ###########################################################
    with open('Cipher.txt', "r") as c_file, open('Key.txt','r') as k_file:
        cipher = c_file.read() 
        keyword = k_file.read()
    ########################################################################
    s = int(input("Enter Shift: "))
    ctext = ''
    for char in cipher:
        if char.isupper():
            ctext = ctext + chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
           ctext = ctext + chr((ord(char) - s - 97) % 26 + 97)
        else: 
            ctext = ctext + char
    
################################################################



### Out file ######################################################
print("Message:    ", message)
print("Ciphertext: ", ctext)
with open('Cipher_text.txt', "w+") as out_file:
         out_file.write(ctext)
#######################################################
    