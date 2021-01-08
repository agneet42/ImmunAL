# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 12:58:53 2018
 
@author: USER
"""
 
import csv
from difflib import get_close_matches 
 
file1 = csv.reader(open('modifiednames.csv','r'))
listofproteins = []
for lines in file1:
    listofproteins.append(lines[0])
 
file2 = open('uniprot.txt','r')
completedetails = []
original_names = []
for lines in file2:
    tab_separated = lines.split('\t')
    temp = []
    temp.append(tab_separated[0])
    temp.append(tab_separated[3].rstrip('\n'))
    original_names.append(tab_separated[3].rstrip('\n'))
    completedetails.append(temp)
     
top_matches = []
original_modified_names = []
 
for string in original_names:
    new_string = string
    if(new_string.find('(') != - 1):
        open1 = []
        close = []
        for pos in range(0,len(new_string)):
            if(new_string[pos] == '('):
                open1.append(pos)
            elif(new_string[pos] == ')'):
                close.append(pos)
        diff = 0
        for index in range(0,len(open1)):
            start = open1[index] - diff
            end = close[index] - diff
            if(end != (len(new_string)-1)):
                new_string = new_string[:start] + new_string[end+1:]
            else:
                new_string = new_string[:start]
            diff = diff + (end-start+1)
    if(new_string.find(';') != -1):
        position = new_string.find(';')
        new_string = new_string[:position]
    if('\t' in new_string):
        new_string.strip('\t')
    new_string.strip(' ')
    original_modified_names.append(new_string)
 
print("done")
count = 0
for values in listofproteins:
    top_matches.append(get_close_matches(values,original_modified_names))
    count = count + 1
    print(count)

file3 = csv.writer(open('modifiednames_modifieduniprot.csv','w'))
 
for values in top_matches:
    file3.writerow(values)
