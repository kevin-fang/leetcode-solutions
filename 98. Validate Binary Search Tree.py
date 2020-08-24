# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder_traversal(self, node):
        if node == None:
            return
        yield from self.inorder_traversal(node.left) 
        yield node.val
        yield from self.inorder_traversal(node.right)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = None
        for i in self.inorder_traversal(root):
            if prev is None:
                prev = i
                continue;
            if prev >= i:
                return False
            prev = i
        return True
