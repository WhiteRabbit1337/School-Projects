# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:06:34 2021

@author: Ryan Nevitt (Rabbit)
websites:
https://www.chegg.com/homework-help/questions-and-answers/problem-gc-content-dna-string-given-percentage-symbols-string-c-g--example-gc-content-agct-q68258036
http://wpressutexas.net/oldcoursewiki/index.php?title=User:Rcardenas:Python1
https://www.sprjdfn.cn/index.php/rosalind/gc/
https://www.learnpython.org/en/String_Formatting
https://www.codecademy.com/forum_questions/51382b87954cc276830008f9
"""


### In File ########################################################
with open('rosalind_gc.txt', 'r') as in_file:
    GCcontent = []
    ids = []
    dna = ''
    while True:
        line = in_file.readline()
        if not line:
            break
        line = line.strip()
        if "Rosalind" in line:
            if len(dna) > 0:
                count = 0
                for char in dna:
                    if char=='G' or char=='C':
                        count += 1
                GCcontent.append(count*100/len(dna))
            idstr = line[1:]
            ids.append(idstr)
            dna = ''
        else:
            dna += line
 ##############################################################          


    #### Percent G C content #################            
    count = 0
    for char in dna:
        if char=='G' or char=='C':
            count += 1
    GCcontent.append(count*100/len(dna))
    #########################################  
    
    ### print all ###########
    for i in range(len(ids)):
        print(ids[i])
        print(GCcontent[i])
    #########################
        

    ### find maximum ########
    maximum = 0
    max_id = 0
    for i in range(len(ids)):
        if GCcontent[i] > maximum: 
            maximum = GCcontent[i]
            max_id = i
    ##########################
    
    ### out file #######
    print()
    print("Max:")
    print(ids[max_id])
    print("%.6f"%(maximum))
    with open("out_ GC.txt", "w") as out_file:
        out_file.write("%s \n%.6f" % (ids[max_id], maximum))   #format for out file
    ##################### 
        