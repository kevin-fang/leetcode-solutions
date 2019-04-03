# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        d = deque()
        
        d.append(root)
        
        nodes = []
        while len(d) > 0:
            length = len(d)
            new_list = []
            for i in range(length):
                node = d.popleft()
                new_list.append(node.val)
                if node.left != None:
                    d.append(node.left)
                if node.right != None:
                    d.append(node.right)
            
            nodes.append(new_list)
            
        return nodes
