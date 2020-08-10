# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:21:30 2020

@author: win 10
"""
# =============================================================================
# finding the length of linked list using recursion and iteration
# =============================================================================

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def length_iter(self):
        temp=self.head
        i=0
        while(temp):
            i=i+1
            temp=temp.next
        return i
    def get_len_rec(self, node):
        if (node==None):
            return 0
        else:
            return 1 +self.get_len_rec(node.next)
    def len_rec(self):
        return self.get_len_rec(self.head)
    def push(self, ele):
        new_node=Node(ele)
        new_node.next=self.head
        self.head=new_node
if __name__=="__main__":
    llist=LinkedList()
    llist.push(5)
    llist.push(5)
    llist.push(5)
    llist.push(5)
    llist.push(5)
    llist.push(5)
    print("Iteratively \t",llist.length_iter())
    print("Recursively \t",llist.len_rec())