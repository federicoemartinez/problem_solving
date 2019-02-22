# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        added = 0
        opened = 0
        for each in S:
            if each == "(":
                opened+=1
            if each == ")":
                opened-=1
                if opened < 0:
                    opened = 0
                    added +=1
        added += opened
        return added
