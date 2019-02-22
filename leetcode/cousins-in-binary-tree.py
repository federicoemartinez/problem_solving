#  https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        a = self.find(root,x,0)
        b = self.find(root,y,0)
        return a[0] == b[0] and a[1] != b[1]
    
    def find(self,root, x, level):
        if root is None: return None
        if root.val == x:
            return (level, None)
        else:
            if root.left is not None:
                if root.left.val == x:
                    return (level+1, root.val)
                a = self.find(root.left, x, level+1)
                if a is not None: return a
            if root.right is not None:
                if root.right.val == x:
                    return (level+1, root.val)
                a = self.find(root.right, x, level+1)
                if a is not None: return a
    
