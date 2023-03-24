# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:08:30 2021

@author: Ryan Nevitt (Rabbit)
"""

rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
splitted_rna = []

while rna:
    splitted_rna.append(rna[:3])
    rna = rna[3:]


for codon in splitted_rna:
    if codon == 'AUG':
        print('M', end="")
    elif codon == 'GCC' or codon == 'GCG' or codon == 'GCU' or codon == 'GCA':
        print('A', end="")
    elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
        print('R', end="")
    elif codon == 'CCC' or codon == 'CCU' or codon == 'CCA' or codon == 'CCG':
        print('P', end="")
    elif codon == 'ACC' or codon == 'ACU' or codon == 'ACA' or codon == 'ACG':
        print('T', end="")
    elif codon == 'GAA' or codon == 'GAG':
        print('E', end="")
    elif codon == 'GAU' or codon == 'GAC':
        print('E', end="")
    elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
        print('I', end="")
    
