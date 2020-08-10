# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:51:19 2020

@author: win 10
"""
# =============================================================================
# circular linked list insert
# =============================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.last=None
    def insert_empty(self,ele):
        if(self.last!=None):
            return self.last
        new_node=Node(ele)
        self.last=new_node
        self.last.next=self.last
    def insert_beg(self,ele):
        if(self.last==None):
            return self.insert_empty(ele)
        new_node=Node(ele)
        new_node.next=self.last.next
        self.last.next=new_node
    def insert_end(self,ele):
        if(self.last==None):
            return self.insert_empty(ele)
        new_node=Node(ele)
        new_node.next=self.last.next
        self.last.next=new_node
        self.last=self.last.next
    def insert_after(self,ele,item):
        if(self.last==None):
            return self.insert_empty(ele)
        new_node=Node(ele)
        temp=self.last.next
        if(self.last.data==item):
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=self.last.next
            return
        while(temp!=self.last):
            if(temp.data==item):
                new_node.next=temp.next
                temp.next=new_node
                return
            temp=temp.next
        return
    def print_list(self):
        temp=self.last.next
        if(self.last is not None):
            while(temp!=self.last):
                print(temp.data)
                temp=temp.next
            
if __name__=="__main__":
    llist=LinkedList()
    llist.insert_empty(6)
    llist.insert_beg(4)
    llist.insert_beg(2)
    llist.insert_end(8)
    llist.insert_end(12)
    llist.insert_after(10,8)
    llist.print_list()