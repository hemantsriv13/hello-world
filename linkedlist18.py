# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:36:02 2020

@author: win 10
"""
# =============================================================================
# prg to segregate odd and even nodes
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
    def odd_even(self):
        p_end=self.head
        while(p_end.next):
            p_end=p_end.next
        cur=self.head
        prev=None
        new_end=p_end
        while(cur.data%2!=0 and cur!=None):
            new_end.next=cur
            cur=cur.next
            new_end.next.next=None
            new_end=new_end.next
        if(cur.data%2==0):
            self.head=cur
            while(cur!=p_end):
                if(cur.data%2==0):
                    prev=cur
                    cur=cur.next
                else:
                    prev.next=cur.next
                    new_end.next=cur
                    new_end.next.next=None
                    new_end=cur
                    cur=prev.next
        else:
            prev=cur
            if(new_end!=p_end and p_end.data%2!=0):
                prev.next=p_end.next
                p_end.next=None
                new_end.next=p_end
        #print(cur.data)
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    llist=LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.odd_even()