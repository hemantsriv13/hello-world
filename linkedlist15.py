# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:50:26 2020

@author: win 10
"""
# =============================================================================
# prg to swap data pairwise and to exchange first and last nodes
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
    def double_swap(self):
        temp=self.head
        while(temp!=None and temp.next!=None):
            temp.data,temp.next.data=temp.next.data,temp.data
            temp=temp.next.next
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def last_to_front(self):
        prev=self.head
        cur=self.head
        while(prev.next.next!=None):
            cur=cur.next
            prev=prev.next
        cur=cur.next
        #print(cur.data, prev.data)
        temp=self.head.next
        #print(temp.data)
        prev.next=None
        prev.next=self.head
        prev.next.next=None
        cur.next=temp
        self.head=cur
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        
if __name__=="__main__":
    llist=LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.double_swap()
    llist.last_to_front()