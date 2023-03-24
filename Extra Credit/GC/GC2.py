# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:49:12 2021

@author: Ryan Nevitt (Rabbit)
"""

from utils import read_fasta, gc_content


if __name__ == '__main__':
    sequences = read_fasta('rosalind_gc.txt')

    max_gc = 0
    max_id = None

    for id, s in sequences.items():
        gc = gc_content(s)

        if gc > max_gc:
            max_gc = gc
            max_id = id

    print (max_id)
    print (max_gc * 100)