# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:53:56 2020

@author: win 10
"""
# =============================================================================
# prg to search an element in linked list using iteration and recursion
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
    def search(self,ele):
        temp=self.head
        while(temp):
            if(temp.data==ele):
                return True
            temp=temp.next
        return False
    def get_rec_search(self,node,ele):
        if(not node):
            return False
        if(node.data==ele):
            return True
        return self.get_rec_search(node.next,ele)
    def rec_search(self,ele):
        return self.get_rec_search(self.head,ele)
if __name__=="__main__":
    llist=LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    print("Iteratively",llist.search(5))
    print("Recursivelt",llist.rec_search(7))