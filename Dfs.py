from collections import deque

class Node:
    def __init__(self, value):   #constructor
        self.value = value
        self.left = None
        self.right = None

# create a binary tree
#        1    
#       / \
#      2   3
#     / \   \
#    4   5   6
root = Node(1)
root.left = Node(2)  
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

def dfs_preorder(root):
    stack = deque()
    stack.append(root)
    
    while stack:
        node = stack.pop()
        print(node.value)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

dfs_preorder(root)
# 1245


   