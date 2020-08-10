# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:58:43 2020

@author: win 10
"""
# =============================================================================
# prg to search element in rotated array
# =============================================================================

def search(arr,low,high,x):
    mid=low+(high-low)//2
    if(x==arr[mid]):
        return mid
    if(x<arr[mid]):
        #print("1")
        if(x<arr[0]):
            #print("2")
            return search(arr,mid+1,high,x)
        elif(x>arr[0]):
            #print("3")
            return search(arr,low,mid-1,x)
        else:
            return 0
    elif(x>arr[mid]):
        return search(arr,mid+1,high,x)
    else:
        return -1
arr=[3,4,5,6,7,1,2]
found=search(arr,0,len(arr)-1,4)
print(found)    