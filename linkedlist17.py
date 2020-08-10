# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:20:52 2020

@author: win 10
"""
# =============================================================================
# prg to find the intersection node
# =============================================================================
class Node:
    def __init__(self,data,flag):
        self.data=data
        self.next=None
        self.flag=flag
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,ele):
        new_node=Node(ele,0)
        new_node.next=self.head
        self.head=new_node
def intersection(ll1,ll2):
    p1=ll1.head
    p2=ll2.head
    while(p1 or p2):       
        if(p1):
            if(p1.flag!=1):
                p1.flag=1
                p1=p1.next
            else:
                print("intersection node in p1", p1.data)
                break
        if(p2):
            if(p2.flag!=1):
                p2.flag=1
                p2=p2.next
            else:
                print("intersection node in p2", p2.data)
                break
if __name__=="__main__":
    llist1=LinkedList()
    llist2=LinkedList()
    llist1.push(30)
    llist1.push(15)
    llist1.push(9)
    llist1.push(6)
    llist1.push(3)
    llist1.push(2)
    llist2.push(10)
    llist2.push(3)
    llist2.push(1)
    llist2.head.next=llist1.head.next.next.next.next
    intersection(llist1,llist2)