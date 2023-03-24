# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:02:49 2021

@author: Rabbit (Ryan Nevitt)
websites:
https://neilsonwilson.github.io/translating-RNA-into-protein.html
https://github.com/mtarbit/Rosalind-Problems/blob/master/e008-prot.py
"""


### In file #############################################################
with open('rosalind_prot.txt', "r") as in_file:
     s = in_file.read()     
     s = s.strip()
#########################################################################
    


### RNA Dictionary ############################################################
def Protein(RNA):

    RNAcodons ={"UUU":"F", "UGG":"W", "AUU":"I", "GUC":"V",
                "UUC":"F", "UGA":"",  "AUC":"I", "GUA":"V",
                "UUA":"L", "UAG":"",  "AUA":"I", "GUG":"V",
                "CUU":"L", "UAA":"",  "AUG":"M", "GCU":"A",
                "UUG":"L", "CCU":"P", "ACU":"T", "GCC":"A",
                "CUU":"L", "CCC":"P", "ACC":"T", "GCA":"A",
                "CUC":"L", "CCA":"P", "ACA":"T", "GCG":"A",
                "CUA":"L", "CCG":"P", "ACG":"T", "GAU":"D",
                "CUG":"L", "CAU":"H", "AAU":"N", "GAC":"D",
                "UCU":"S", "CAC":"H", "AAC":"N", "GAA":"E",
                "UCC":"S", "CAA":"Q", "AAA":"K", "GAG":"E",
                "UCA":"S", "CAG":"Q", "AAG":"K", "GGU":"G",
                "UCG":"S", "CGU":"R", "AGU":"S", "GGC":"G",
                "UAU":"Y", "CGC":"R", "AGC":"S", "GGA":"G",
                "UAC":"Y", "CGA":"R", "AGA":"R", "GGG":"G",
                "UGU":"C", "CGA":"R", "AGG":"R",
                "UGC":"C", "CGG":"R", "GUU":"V",}
                    
                      
    
    codons = []
    for i in range(0,len(RNA),3):
        codons.append(RNA[i:i+3])
    protein = ''.join([RNAcodons[codon] for codon in codons])
    return protein
##############################################################################



### Out file ###############################
print(Protein(s))
with open('Ros_Out.txt', "w+") as out_file:
           out_file.write(Protein(s))
#############################################
