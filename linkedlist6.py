# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:57:37 2020

@author: win 10
"""
# =============================================================================
# prg to find the Nth node element
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
    def nth_node(self,n):
        temp=self.head
        ind=0
        while(temp):
            if(ind==n):
               return temp.data 
            temp=temp.next
            ind+=1
        return False
    def rec_nth_node(self,n):
        count=0
        return self.get_rec_nth_node(self.head,count,n)
    def get_rec_nth_node(self,node,count,n):
        if(node):
            if(count==n):
                return node.data
            else:
                return self.get_rec_nth_node(node.next,count+1,n)
        else:
            return False
if __name__=="__main__":
    llist=LinkedList()
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print(llist.nth_node(2))
    print(llist.rec_nth_node(3))