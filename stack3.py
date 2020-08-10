#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:38:50 2020

@author: hemant
"""
# =============================================================================
# program to execute queue using stacks with costly dequeue
# =============================================================================

class Queue:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    def enqueue(self, ele):
        self.st1.append(ele)
        print(self.st1)
    def dequeue(self):
        while(len(self.st1)!=0):
            self.st2.append(self.st1[-1])
            self.st1.pop()
            
        while(len(self.st2)!=0):
            x=self.st2[-1]
            self.st2.pop()
            return x
    def printQueue(self):
        print(self.st2)
        
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())          