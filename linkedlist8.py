# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:14:35 2020

@author: win 10
"""
# =============================================================================
# prg to find middle element for odd and even length linked list
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
        temp=self.head
        l=0
        while(temp):
            l+=1
            temp=temp.next
        return l
    def dp_mid_element(self):
        p1=self.head
        p2=self.head
        p3=self.head
        c=0
        while(p2):
            if(p2.next.next==None):
                p1=p1.next
                #print("1")
                c+=1
                break
            else:
                p2=p2.next.next
                p1=p1.next
                c+=1
                #print("2")
                
        if(int(c%2)!=0):
            for i in range(c-1):
                p3=p3.next
        print(p3.data)
        print(p1.data)
        return
if __name__=="__main__":
    llist=LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.dp_mid_element()