# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:45:56 2020

@author: win 10
"""
# =============================================================================
# prg for intersection of two sorted ll
# =============================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self, ele):
        new_node=Node(ele)
        new_node.next=self.head
        self.head=new_node
def merge(llist1,llist2):
    p1=llist1.head
    p2=llist2.head
    llist3=LinkedList()
    while(p1 and p2):
        if(p1.data==p2.data):
            llist3.push(p1.data)
            p1=p1.next
            p2=p2.next
        elif(p1.data<p2.data):
            p1=p1.next
        else:
            p2=p2.next
    temp=llist3.head
    while(temp):
        print(temp.data)
        temp=temp.next
        
if __name__=="__main__":
    llist1=LinkedList()
    llist2=LinkedList()
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)
    llist2.push(4)
    llist2.push(3)
    llist2.push(1)
    merge(llist1,llist2)