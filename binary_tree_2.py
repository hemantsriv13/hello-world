# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:34:42 2020

@author: win 10
"""
# =============================================================================
# level order traversal using queue
#               1
#             2   3
#           4  5 6  7
#                  8
# finding largest distance between 2 nodes
# finding height of the tree
# =============================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(node):
    if(node is None):
        return 0
    else:
        print("going left")
        lheight=height(node.left)
        print("lh", node.data, lheight)
        print("going right")
        rheight=height(node.right)
        print("rh", node.data, rheight)
        return 1+max(lheight,rheight)
def levelorder(root):
    queue=[]
    if root is None:
        return
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data)
        node=queue.pop(0)
        if(node.left is not None):
            queue.append(node.left)
        if(node.right is not None):
            queue.append(node.right)
def diameter(node):
    lh=0
    rh=0
    if(node is None):
        return 0
    else:
        lheight=height(node.left)
        rheight=height(node.right)
        return 1+max(lheight,rheight)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(8)
print(height(root))
#levelorder(root)
#print(height(root))
print(diameter(root.left)+diameter(root.right))
#print(diameter(root.right))