#https://leetcode.com/problems/range-sum-of-bst/description/
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def _sum(self,root, L, R):
        res = 0
        if root.val >= L and root.val <= R: 
            res = root.val
        if root.val > L and not(root.left is None):
            res += self._sum(root.left, L, R)
        if root.val < R and not(root.right is None):
            res += self._sum(root.right, L, R)
        return res
            
    
    def rangeSumBST(self, root, L, R):
        return self._sum(root,L,R)
        
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
