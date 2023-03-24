# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:36:40 2021

@author: Ryan Nevitt (Rabbit)\
https://www.chegg.com/homework-help/questions-and-answers/problem-gc-content-dna-string-given-percentage-symbols-string-c-g--example-gc-content-agct-q68258036
http://wpressutexas.net/oldcoursewiki/index.php?title=User:Rcardenas:Python1
https://www.sprjdfn.cn/index.php/rosalind/gc/
https://www.learnpython.org/en/String_Formatting
https://www.codecademy.com/forum_questions/51382b87954cc276830008f9
"""

with open("rosalind_gc.txt", "r") as in_file:
    seq_name = in_file.readline().replace("\n", "")
    seq_content = ""
    ans_gc = 0.0
    ans_name = ""
    while True:
        line = in_file.readline().replace("\n", "")
        if (line == "" or line[0] == '>'):
            now_gc = (seq_content.count('G') + seq_content.count('C'))* 1.0 / len(seq_content)
            if (now_gc > ans_gc):
                ans_gc = now_gc
                ans_name = seq_name
            if (line == ""):
                break
            seq_name = line[1:]
            seq_content = ""
            continue
        seq_content = seq_content + line
        
        
    with open("out_ GC.txt", "w") as out_file:
        out_file.write("%s \n%.6f" % (ans_name, ans_gc * 100.0))   #format for out file
    print(ans_name)
    print("%.6f" % (ans_gc*100))