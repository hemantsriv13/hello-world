# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:22:33 2020

@author: win 10
"""
# =============================================================================
# prg to delete a linkedlist
# =============================================================================

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,ele):
        new_node=Node(ele) #creates a new node with data=ele, next=none
        new_node.next=self.head #makes next of the new node as head
        self.head=new_node # moves the head to point to new node
    def delete_list(self):
        current=self.head #initialize the current node
        while(current):
            prev=current.next #move to next node
            print(current.data)
            del current.data #delete current node
            current=prev #point current to next(previous) node
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
    llist.print_list()
    llist.delete_list()