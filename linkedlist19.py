# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:58:15 2020

@author: win 10
"""

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
    def reverse(self):
        prev=None
        cur=self.head
        while(cur):
            next=cur.next
            print("one",cur.data)
            cur.next=prev
            print("two",cur.data)
            prev=cur
            print("three",cur.data,prev.data)
            cur=next
            print("four",prev.data)
        self.head=prev
        t=self.head
        while(t):
            print(t.data)
            t=t.next
if __name__=="__main__":
    llist=LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.reverse()