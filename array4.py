# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:12:45 2020

@author: win 10
"""

def zeroes(arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]!=0):
            arr[count]=arr[i]
            count+=1
    while(count<len(arr)):
        arr[count]=0
        count+=1
arr=[1,9,8,4,0,0,2,7,0,6,0,9]
zeroes(arr)
print(arr)