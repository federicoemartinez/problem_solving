# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        # print None if root1 is None else root1.val, None if root2 is None else root2.val
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None:
            return root2 is None
        if root2 is None:
            return False
        if root1.val != root2.val: return False

        right_matches = (root1.right is None and root2.right is None) or (
                root1.right is not None and root2.right is not None and root1.right.val == root2.right.val)
        left_matches = (root1.left is None and root2.left is None) or (
                root1.left is not None and root2.left is not None and root1.left.val == root2.left.val)
        if right_matches and left_matches:
            return self.flipEquiv(root1.right, root2.right) and self.flipEquiv(root1.left, root2.left)
        flip1_matches = (root1.right is None and root2.left is None) or (
                root1.right is not None and root2.left is not None and root1.right.val == root2.left.val)
        filp2_matches = (root1.left is None and root2.right is None) or (
                root1.left is not None and root2.right is not None and root1.left.val == root2.right.val)
        if flip1_matches and filp2_matches:
            return self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)
        return False
