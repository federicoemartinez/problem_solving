https://leetcode.com/problems/distinct-subsequences-ii/description/
"""
Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 

 

Note:

S contains only lowercase letters.
1 <= S.length <= 2000
"""

from collections import defaultdict

class Solution:
        
    def countSubSeq(self, last_index, i, S, counter):
        if i in counter: return counter[i]
        if i == 0:
            counter[i] = 1
            return 1
        else:
            res = 2 * self.countSubSeq(last_index, i-1, S, counter)
            dup = 0
            if S[i-1] in last_index:
                dup = self.countSubSeq(last_index, last_index[S[i-1]], S, counter)
            counter[i] = res - dup
            last_index[S[i-1]] = i-1
            return res - dup
        
        

    def distinctSubseqII(self, S):
        last_index = {}
        counter = {}
        #l = [self.countSubSeq(last_index, j, S, counter) for j in range(len(S)+1)]
        #print(l)
        res = self.countSubSeq(last_index, len(S), S, counter) - 1
        return res % (10**9 + 7)
        
        """
        :type S: str
        :rtype: int
        """
