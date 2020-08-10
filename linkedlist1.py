#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:25:48 2020

@author: hemant
"""


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    llist.head.next=second
    second.next=third
    llist.push(4)
    llist.printList()