# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 01:01:04 2020

@author: win 10
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if(root):
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(root.data)
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    inorder(root)
    print(" ")
    preorder(root)
    print(" ")
    postorder(root)
    print(" ")