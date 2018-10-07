# https://leetcode.com/problems/string-to-integer-atoi/description/
"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

"""

class Solution:
    def myAtoi(self, str):
        trimmed_string = str.strip()
        sign = 1
        if len(trimmed_string) == 0:
            return 0
        if trimmed_string[0] == "-": sign = -1
        if  trimmed_string[0] in ("-", "+"): trimmed_string = trimmed_string[1:]
        i = 0
        while(i < len(trimmed_string) and trimmed_string[i].isnumeric()):
            i+=1
        if i == 0: return 0
        res = int(trimmed_string[0:i]) * sign
        if res > 2 ** 31 -1: return  2**31 -1
        if res < - 2 ** 31: return  -2 ** 31
        return res
        
