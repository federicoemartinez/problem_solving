# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        return [int("".join(x)) for x in self.numsSameConsecDiffAux(0, None, N, K)] + ([0] if N == 1 else [])
        
    def numsSameConsecDiffAux(self, i, prev, N, K):
        if N == 0: return [[]]
        if i == 0:
            res = []
            for j in range(1,10):
                res.extend( [[str(j)]+l for l in self.numsSameConsecDiffAux(i+1, j, N-1, K)] )
            return res
        res = []
        for j in [a for a in set([prev+K, prev-K])  if a < 10 and a >= 0]:
            res.extend([[str(j)]+l for l in self.numsSameConsecDiffAux(i+1, j, N-1, K)])
        return res
