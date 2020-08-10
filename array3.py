# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:44:54 2020

@author: win 10
"""

def search_hash(arr,sum1):
    s=set()
    for i in range(0,len(arr)):
        temp=sum1-arr[i]
        if(temp in s):
            print(arr[i],temp)
        s.add(arr[i])
arr=[3,4,5,6,7,1,2]
search_hash(arr,4)   