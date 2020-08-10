# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 01:18:05 2020

@author: win 10
"""
# =============================================================================
# prg to check if ll is palindrome using a stack
# =============================================================================
class Stack:
    def __init__(self):
        self.stack=[]
    def push1(self,ele):
        self.stack.append(ele)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)
    def printStack(self):
        print(self.stack)
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
    def palin(self):
        stack=Stack()
        temp=self.head
        c=0
        while(temp):
            stack.push1(temp.data)
            temp=temp.next
        length=stack.length()
#        stack.printStack()
        temp=self.head
#        while(temp):
#            print(temp.data)
#            temp=temp.next
#        temp=self.head
        for i in range(length):
            n=stack.pop()
#            print(temp.data,n)
            if(temp.data==n):
                #print("1")
                c+=1
            temp=temp.next
        if(c==length):
            print("palindrome")
        else:
            print("not palindrome")
if __name__=="__main__":
    llist=LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    st1=Stack()
    llist.palin()