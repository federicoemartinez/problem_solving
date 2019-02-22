# https://leetcode.com/problems/all-possible-full-binary-trees/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        return self.allPossibleFBTAux(N)
        
    def allPossibleFBTAux(self, N):
        if N == 0:
            return [None]
        if N == 1:
            return [TreeNode(0)]
        if N == 2:
            return []
        res = []
        for i in range(1,N-1,2):
            if N-i-1 < i: break
            left = self.allPossibleFBTAux(i)
            right = self.allPossibleFBTAux(N-i-1)
            
            for l in left:
                for r in right:
                    t = TreeNode(0)
                    t.left = l
                    t.right = r
                    res.append(t)
                    if N-i-1 != i:
                        t = TreeNode(0)
                        t.left = r
                        t.right = l
                        res.append(t)
                        
        return res
            
        
