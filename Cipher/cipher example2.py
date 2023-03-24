# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:00:09 2021

@author: Ryan Nevitt (Rabbit)
"""

with open('Message.txt', "r") as m_file, open('Key.txt','r') as k_file:
    message = m_file.read() 
    key = k_file.read()

def encrypt(message, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    message_int = [ord(i) for i in message]
    print(key_as_int,message_int)
    ciphertext = ''
    for i in range(len(message_int)):
        value = (message_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    message = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        message += chr(value + 65)
    return message

