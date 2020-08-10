# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:37:24 2020

@author: win 10
"""
# =============================================================================
# prg to find lenght of loop
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
    def length(self):
        p1=self.head
        p2=self.head
        while(p2):
            p2=p2.next.next
            p1=p1.next
            #print("1")
            if(p1==p2):
                p3=p1
                #print("2")
                break
        count=1
        while(p2):
            p2=p2.next.next
            p1=p1.next
            count+=1
            #print("3")
            if(p1==p3):
                #print("4")
                break
        print(count)
if __name__=="__main__":
    llist=LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.head.next.next.next=llist.head
    llist.length()