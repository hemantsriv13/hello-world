# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:36:36 2020

@author: win 10
"""
# =============================================================================
# reverse a dll
# =============================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,ele):
        new_node=Node(ele)
        new_node.next=self.head
        if(self.head!=None):
            self.head.prev=new_node
        self.head=new_node
    def reverse(self):
        temp=None
        cur=self.head
        while(cur):
            temp=cur.prev
            cur.prev=cur.next
            cur.next=temp
            cur=cur.prev
        if(temp is not None):
            self.head=temp.prev
    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    llist=LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.print_list()
    llist.reverse()
    llist.print_list()