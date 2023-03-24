"""
Created on Tue Mar 30 18:31:29 2021

@author: Rabbit (Ryan Nevitt)

websites:
https://www.geeksforgeeks.org/vigenere-cipher/
https://geektechstuff.com/2020/01/03/vigenere-cipher-python/
https://www.geeksforgeeks.org/python-numbers-choice-function/a
"""


### Encrypt or Decrypt #################################################
choice = input("Enter 1 for Encryption.\nEnter 2 for Decryption.\n>>> ")
choice = int(choice)
########################################################################





if choice == 1:
     ### User Input ##################################
    message = input("What is the Secret Message?: ")
    keyword = input("What is the key phrase?: ")
    #################################################
    
    # ### In file ##############################
    # with open('Message.txt', "r") as in_file:
    #         file = in_file.read()
    #         # int_list = file.split()
    #         ptext = file 
    ############################################    
   
    s = int(input("Enter Shift: "))
    ctext = ''
    for char in ptext:
        if char.isupper():
            ctext = ctext + chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
           ctext = ctext + chr((ord(char) + s - 97) % 26 + 97)
        else: 
            ctext = ctext + char
    
    
    ctext = ''
    for char in ptext:
        if char.isupper():
            ctext = ctext + chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
           ctext = ctext + chr((ord(char) + s - 97) % 26 + 97)
        else: 
            ctext = ctext + char





### Out file ###
print("Plaintext:", ptext)
print("Ciphertext: ", ctext)
with open('Cipher_text.txt', "w+") as out_file:
         out_file.write(ctext)
    