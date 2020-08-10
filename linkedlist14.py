# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:44:11 2020

@author: win 10
"""
# =============================================================================
# prg to swap nodes
# =============================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,ele):
        new_node=Node(ele)
        new_node.next=self.head
        self.head=new_node
    def swap(self,x,y):
        if(x==y):
            return 
        prevX=None
        currX=self.head
        while(currX!=None and currX.data!=x):
            prevX=currX
            currX=currX.next
        prevY=None
        currY=self.head
        while(currY!=None and currY.data!=y):
            prevY=currY
            currY=currY.next
        if(currX==None or currY==None):
            return
        if(prevX!=None):
            prevX.next=currY
        else:
            self.head=currY
        if(prevY!=None):
            prevY.next=currX
        else:
            self.head=currX
        temp=currX.next
        currX.next=currY.next
        currY.next=temp
        t=self.head
        while(t):
            print(t.data)
            t=t.next
if __name__=="__main__":
    llist=LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.swap(4,2)