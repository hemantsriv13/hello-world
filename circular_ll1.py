# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:14:31 2020

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
        temp=self.head
        new_node.next=self.head
        if(self.head is not None):
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
        else:
            new_node.next=new_node
        self.head=new_node
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
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.printlist()