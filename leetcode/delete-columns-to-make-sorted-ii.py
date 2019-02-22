https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        acum = 0
        def is_sorted(A):
            return all((A[i] <= A[i+1] for i in range(len(A)-1)))
        
        A = [('',x) for x in A]
        
        while not is_sorted(A):
            if any(((A[i][0],A[i][1][0])>(A[i+1][0],A[i+1][1][0]) for i in xrange(len(A)-1))):
                acum+=1
                A = [(pref,suf[1:]) for pref, suf in A]
            else:
                A = [(pref+suf[0],suf[1:]) for pref, suf in A]
        return acum    
