# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:07:27 2020

@author: win 10
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height(node):
    if(node is None):
        return 0
    else:
        lheight=height(node.left)
        rheight=height(node.right)
        return 1+max(lheight,rheight)
def enter(arr,root,i,n):
    if(i<n):
        temp=Node(arr[i])
        root=temp
        root.left=enter(arr, root.left, 2*i+1,n)
        root.right=enter(arr, root.right, 2*i+2,n)
    return root
arr=list(map(int,input().split()))
n=len(arr)
root1=None
root1=enter(arr,root1,0,n)
print(height(root1))
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(8)
print(height(root))