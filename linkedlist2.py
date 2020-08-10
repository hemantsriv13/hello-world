# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:05:16 2020

@author: win 10
"""
# =============================================================================
# prg to delete a node at a given position
# prg to push a node at any point
# =============================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push_in_front(self,ele):
        new_node=Node(ele)
        new_node.next=self.head
        self.head=new_node
    def push_after_node(self,prev_node,ele):
        if prev_node is None:
            print("Previous node not present")
            return
        new_node=Node(ele)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def push_at_end(self,ele):
        new_node=Node(ele)
        if (self.head is None):
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def delete(self,pos):
        if(self.head==None):
            return
        temp=self.head
        if(pos==0):
            self.head=temp.next
            temp=None
            return
        for i in range(pos-1):
            temp=temp.next
            if(temp is None):
                break
        if(temp is None):
            return
        if(temp.next is None):
            return
        next=temp.next.next
        temp.next=None
        temp.next=next            
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data) 
            temp = temp.next
# Code execution starts here 
if __name__=='__main__':   
    # Start with the empty list
    llist = LinkedList()   
    # Insert 6.  So linked list becomes 6->None
    llist.push_in_front(6)  
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push_in_front(7)  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push_in_front(1)  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.push_at_end(4)  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.push_after_node(llist.head.next, 8)   
    print ('Created linked list is:') 
    llist.delete(3)
    llist.printList()