# https://leetcode.com/problems/knight-dialer/description/
"""
A chess knight can move as indicated in the chess diagram below:

https://assets.leetcode.com/uploads/2018/10/12/knight.png
https://assets.leetcode.com/uploads/2018/10/30/keypad.png

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

 

Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46
 

Note:

1 <= N <= 5000
"""

data = [{1:1} for i in range(10)]
movements = dict()
movements[0] = [4,6]
movements[1] = [6,8]
movements[2] = [7,9]
movements[3] = [4,8]
movements[4] = [3,9,0]
movements[5] = []
movements[6] = [1,7,0]
movements[7] = [2,6]
movements[8] = [1,3]
movements[9] = [2,4]




class Solution(object):
    
    
    def options(self,  each, N):
        if N in data[each]:
            return data[each][N]
        res = 0
        for nextv in movements[each]:
            child_opts = self.options(nextv, N-1)
            if child_opts == 0: continue
            res += child_opts
        data[each][N] = res
        return res
    
    def knightDialer(self, N):
        res = 0
        for each in range(10):
            res += self.options(each, N)
        return res % (10**9 + 7)
        """
        :type N: int
        :rtype: int
        """
    
    
