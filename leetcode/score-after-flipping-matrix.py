# https://leetcode.com/problems/score-after-flipping-matrix/
class Solution(object):
   
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def more_zeroes_col(A,j):
            zeroes=0
            ones=0
            for i in range(len(A)):
                if A[i][j] == 0:
                    zeroes+=1
                else:
                    ones+=1
            return zeroes > ones
        
        def flip_col(A,j):
            for i in range(len(A)):
                A[i][j] = 1 - A[i][j]
            
        def sumBinary(A):
            return sum(int("0b"+"".join(str(x) for x in row),2) for row in A)
        
        for i in xrange(len(A)):
            if A[i][0] == 0:
                for j in xrange(len(A[0])):
                    A[i][j] = 1 - A[i][j]
        for j in xrange(1,len(A[0])):
            if more_zeroes_col(A,j):
                flip_col(A,j)
        return sumBinary(A)
