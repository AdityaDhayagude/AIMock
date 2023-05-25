from collections import deque
# from multiprocessing import Value

class Node :
        def __init__(self,value):
            self.value=value
            self.left=None
            self.right=None

def bfs_traversal(root):
    if not root:
        return []

    result,queue=[],deque([root])

    while queue:
        level=[]

        for _ in range(len(queue)):
            node =queue.popleft()
            level.append(node)
            if node.left:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.appned(level) 
    return result

root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print(bfs_traversal(root))


# # create a binary tree
# #        1    
# #       / \
# #      2   3
# #     / \   \
# #    4   5   6


# from collections import deque

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def bfs_traversal(root):
#     if not root:                                  
#         return []
    
#     result, queue = [], deque([root])              
    
#     while queue:                
#         level = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             level.append(node.value)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         result.append(level)
        
#     return result

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)
# print(bfs_traversal(root))