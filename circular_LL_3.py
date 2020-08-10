# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:23:42 2020

@author: win 10
"""
# =============================================================================
# prg for sorted input in circular ll
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
        temp=self.head
        if(temp is None):
            new_node.next=new_node
            self.head=new_node
        elif(temp.data>=new_node.data):
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            self.head=new_node
        else:
            while(temp.next.data<new_node.data and temp.next!=self.head):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def printlist(self):
        temp=self.head
        if(self.head is not None):
            while(True):
                print(temp.data)
                temp=temp.next
                if(temp==self.head):
                    break
if __name__=="__main__":
    llist=LinkedList()
    llist.printlist()
    llist.push(10)
    llist.push(2)
    llist.push(33)
    llist.push(1)
    llist.printlist()