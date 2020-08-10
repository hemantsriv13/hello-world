#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:50:19 2020

@author: hemant
"""
# =============================================================================
# 2 STacks in a single array
# =============================================================================

class Stack:
    def __init__(self):
        self.st=[[],[]]
    def Push(self,push,ele):
        if(len(self.st0)!=0):
            if(push==1):
                self.st[0].append(ele)
            elif(push==2):
                self.st[1].append(ele)
            else:
                print("Not Possible")
                return -99
        else:
            print("Empty queue")
            return -1
    def Pop(self,pop):
        if(len(self.st)!=0):
            if(pop==1):
                x=self.st[0][-1]
                self.st[0][-1].pop()
                return x
            elif(pop==2):
                x=self.st[1][-1]
                self.st[1][-1].pop()
                return x
            else:
                print("Not Possible")
                return -99
        else:
            print("Empty Stack")
            return -100
        
st=Stack()
push=int(input())
n=input()
st.Push(push,n)
