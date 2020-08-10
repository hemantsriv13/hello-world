# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:38:55 2020

@author: win 10
"""
# =============================================================================
# prg to split a circular linked list in two circular linked list
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
    def split1(self,head1,head2):
        p1=self.head
        p2=self.head
        while(p2.next!=self.head and p2.next.next!=self.head):
            p2=p2.next.next
            p1=p1.next
        print(p1.data,p2.data)
        if(p2.next.next==self.head):
            p2=p2.next
        print(p1.data,p2.data)
        head1.head=self.head
        if(self.head.next!=self.head):
            head2.head=p1.next
        p2.next=p1.next
        p1.next=self.head
if __name__=="__main__":
    llist=LinkedList()
    head1=LinkedList()
    head2=LinkedList()
    llist.printlist()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.printlist()
    llist.split1(head1,head2)
    head1.printlist()
    head2`.printlist()