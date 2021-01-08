# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:19:17 2018

@author: USER
"""

file1 = open('result_diseased.txt','r')
file2 = open('result_controlled.txt','r')

arr_diseased = []
arr_controlled = []

for val in file1:
    if(len(val) > 0):
        arr_diseased.append(int(val))
        
for val in file2:
    if(len(val) > 0):
        arr_controlled.append(int(val))

print(len(list(set(arr_diseased) & set(arr_controlled))))