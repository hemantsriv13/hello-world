# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:22:54 2020

@author: win 10
"""
# =============================================================================
# prg to find frequency of the element
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
    def rec_freq(self,ele):
        count=0
        return self.get_rec_freq(self.head,ele,count)
    def get_rec_freq(self,node,ele,count):
        if(not node):
            return count
        else:
            if(node.data==ele):
                count+=1
            return self.get_rec_freq(node.next,ele,count)
if __name__=="__main__":
    llist=LinkedList()
    llist.push(1)
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print(llist.rec_freq(0))
            