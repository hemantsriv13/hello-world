# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:44:43 2020

@author: win 10
"""
# =============================================================================
# delete a node in dll
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
    def delete(self,ele):
        temp=self.head
        if(self.head.data==ele):
            self.head=self.head.next
            self.head.prev=None
        else:
            while(temp.next):
                if(temp.next.data==ele):
                    next1=temp.next.next
                    temp.next.prev=None
                    prev1=temp.next.next.prev
                    temp.next=next1
                    prev1=temp
                    return
                else:
                    temp=temp.next
    def print_list(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    llist=LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.delete(3)
    llist.print_list()