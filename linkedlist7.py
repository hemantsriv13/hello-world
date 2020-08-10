# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:01:12 2020

@author: win 10
"""
# =============================================================================
# prg to find nth node from the end using iteration and double pointer methods
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
    def iter_nth_end(self,pos):
        l=0
        temp=self.head
        while(temp):
            l+=1
            temp=temp.next
        pos1=l-pos
        if(pos>l):
            return False
        temp=self.head
        for i in range(0,pos1):
            temp=temp.next
        return temp.data
    def iter_nth_end_dp(self,pos):
        p1=self.head
        p2=self.head
        temp=self.head
        l=0
        while(temp):
            l+=1
            temp=temp.next
        if (pos>l):
            return False
        for i in range(pos):
            p2=p2.next
        while(p2):
            p2=p2.next
            p1=p1.next
        return p1.data
if __name__=="__main__":
    llist=LinkedList()
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print(llist.iter_nth_end(1))
    print(llist.iter_nth_end_dp(2))