# https://leetcode.com/problems/number-of-squareful-arrays/
import math
from collections import deque
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return self.numSquarefulPermsAux(deque(A), None)
        
    def isPerfectSquareSum(self,a,b):
        x = math.floor(math.sqrt(a+b))
        
        res = x * x == a + b
        #print a,b, x, res
        return res
        
        
    def numSquarefulPermsAux(self, A,init_val):
        if len(A) == 0:
            return 1
        i = 0
        acum = 0
        l = len(A)
        d = {}
        while(i < l):
            next_ = A.pop()
            if next_ in d:
                #acum+=d[next_]
                pass
            elif init_val is None or self.isPerfectSquareSum(init_val, next_):
                res = self.numSquarefulPermsAux(A, next_)
                acum=acum + res
                d[next_] = res
            else:
                d[next_] = 0
            A.appendleft(next_)
            i+=1
        return acum
