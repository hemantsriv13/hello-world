# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:03:55 2020

@author: win 10
"""

def emerald(a,b):
    if(a==0 or b==0):
        em=0
    else:
        em=int((a+b)/3)
    return em
t=int(input())
l2=[]
for i in range(t):
    l1=list(map(int,input().split()))
    l2.append(emerald(int(l1[0]),int(l1[1])))
for i in range(len(l2)):
    print(l2[i])