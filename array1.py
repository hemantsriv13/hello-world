# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:16:59 2020

@author: win 10
"""

def binary_search(arr,low,high,x):
    if(low<=high):
        mid=int((high-low)/2)+low
        if(arr[mid]==x):
            return mid
        if(arr[mid]<x):
            return binary_search(arr,mid+1,high,x)
        else:
            return binary_search(arr,low,mid-1,x)
    else:
        return -1
arr=[1,2,3,4,5,6,7,8,9]
found=binary_search(arr,0,len(arr)-1,1)
print(found)    