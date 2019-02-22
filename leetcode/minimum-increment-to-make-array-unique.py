# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        i = 0
        movs = 0
        while(i<len(A)-1):
            j = i+1
            if A[j] < A[i]:
                movs+=A[i]-A[j]
                A[j] = A[i]
            if A[j] == A[i]:
                A[j]+=1
                movs+=1
            i+=1
        return movs
        
