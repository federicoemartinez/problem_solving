#https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        r = root
        self.insertIntoBSTAux(root, val)
        return r
    
    
    def insertIntoBSTAux(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
                return
            self.insertIntoBSTAux(root.left, val)
        if val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
                return
            self.insertIntoBSTAux(root.right, val)
