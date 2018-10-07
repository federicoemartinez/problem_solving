# https://leetcode.com/problems/reverse-integer/description/
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        if x_str[0] == "-":
            sign = -1
            x_str =  x_str[1:]
        else:
            sign = 1
        val = int(x_str[::-1]) * sign
        if val < - 1 * (2 ** 31): val = 0
        if val > (2 ** 31 - 1):  val = 0
        return val
        
