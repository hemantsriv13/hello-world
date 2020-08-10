# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:42:13 2020

@author: win 10
"""
# =============================================================================
# prg to check for loop using a flag attribute
# =============================================================================
class Node:
    def __init__(self,data,flag):
        self.data=data
        self.flag=flag
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,ele):
        new_node=Node(ele,0)
        new_node.next=self.head
        self.head=new_node
    def check_loop(self):#without hashing
        temp=self.head
        while(temp):
            temp.flag=1
            temp=temp.next
            if(temp!=None and temp.flag==1):
                print("loop")
                return
        print("no loop")
        return
if __name__=="__main__":
    llist=LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.head.next.next.next=llist.head.next
    llist.check_loop()