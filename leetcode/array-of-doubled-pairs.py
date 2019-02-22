# https://leetcode.com/problems/array-of-doubled-pairs/
from collections import Counter
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        c = Counter(A)
        A.sort(key=abs)
        for each in A:
            #print each, c
            if c[each] == 0: continue
            if c[2*each] > 0:
                c[2*each]-=1
                c[each]-=1
            else:
                return False
        return True
    
    
    
