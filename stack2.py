#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:01:06 2020

@author: hemant
"""
# =============================================================================
# program to execute queue using stacks with costly enqueue
# =============================================================================

class Queue:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    def enqueue(self,ele):
        while(len(self.st1)!=0):
            self.st2.append(self.st1[-1])
            self.st1.pop()
            
        self.st2.append(ele)
        
        while(len(self.st2)!=0):
            self.st1.append(self.st2[-1])
            self.st2.pop()
            
        print(self.st1)
    def dequeue(self):
        if(len(self.st1)==0):
            print("Empty queue")
            return -99
        x=self.st1[-1]
        print(x)
        self.st1.pop()
        return x
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()          