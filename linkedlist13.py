# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:31:34 2020

@author: win 10
"""
# =============================================================================
# prg to replace all duplicates from a sorted linked list
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
        self.head=new_node
    def remove_dup(self):
        p1=self.head
        p2=self.head
        c=0
        while(p2):
#            print("p1",p1.data,"p2",p2.data)
            if(p2.data==p1.data):
                p2=p2.next
#                print("p2 skips")
            else:
                p1.next=p2
                p1=p1.next
#                print("p1 moves")
                c+=1
        if(p1.next):
            if(p1.data==p1.next.data):
                p1.next.data=None
                p1.next=None
        c+=1
        temp=self.head
        for i in range(c):
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    llist=LinkedList()
    llist.push(4)
    llist.push(4)
    llist.push(4)
    llist.push(4)
    llist.push(4)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(2)
    llist.push(1)
    llist.remove_dup()