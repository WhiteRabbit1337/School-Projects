# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 02:34:18 2021

@author: Rabbit (Ryan Nevitt)
"""

s = 'AAAACCCGGT'
print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))