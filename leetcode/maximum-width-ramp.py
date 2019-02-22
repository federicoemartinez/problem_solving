# https://leetcode.com/problems/maximum-width-ramp/
class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        l = [(b,a) for (a,b) in enumerate(A)]
        l.sort()
        top = len(A)-1
        positions = set(range(len(A)))
        acum = 0
        for each in l:
            while(top not in positions):
                top-=1
                if top < 0: return acum
            cand = top -each[1]
            positions.remove(each[1])
            if cand > acum:
                acum = cand
        return acum
