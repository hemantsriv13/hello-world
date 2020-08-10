# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:48:46 2020

@author: win 10
"""
# =============================================================================
# prg to insert element in dll
# =============================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push_beg(self,ele):
        new_node=Node(ele)
        new_node.next=self.head
        if(self.head==None):
            self.head=new_node
            return
        self.head.prev=new_node
        new_node.prev=None
        self.head=new_node
    def push_after(self,ele,item):
        new_node=Node(ele)
        temp=self.head
        while(temp!=None):
#            print("1")
            if(temp.data==item):
                new_node.next=temp.next
                temp.next.prev=new_node
                temp.next=new_node
                new_node.prev=temp
#                print("2")
                return
            else:
                temp=temp.next
#                print("3")
    def push_bef(self,ele,item):
        new_node=Node(ele)
        temp=self.head
        while(temp.next):
            if(temp.next.data==item):
                new_node.next=temp.next
                temp.next.prev=new_node
                temp.next=new_node
                new_node.prev=temp
                return
            temp=temp.next
    def push_end(self,ele):
        new_node=Node(ele)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def print_list(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    llist=LinkedList()
    llist.push_beg(5)
    llist.push_beg(4)
    llist.push_beg(3)
    llist.push_beg(2)
    llist.push_beg(1)
    llist.push_after(10,4)
    llist.push_bef(11,3)
    llist.push_end(100)
    llist.print_list()
    print(llist.head.next.next.prev.data)