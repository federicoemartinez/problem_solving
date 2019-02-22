#https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        skyline_left_right = [max(grid[i]) for i in xrange(len(grid))]
        skyline_top_bottom = [max((grid[i][j] for i in xrange(len(grid)))) for j in xrange(len(grid[0]))]
        acum = 0
        A = grid
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                acum +=  min(skyline_left_right[i]-A[i][j], skyline_top_bottom[j] - A[i][j])
        return acum
