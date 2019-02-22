# https://leetcode.com/problems/is-subsequence/
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rrtypetype: bool
        """
        i = 0
        j = 0
        while j < (len(s)):
          cool=False
          while(i< len(t)):
            if t[i] == s[j]:
                i+=1
                cool=True
                break
            else:
                i+=1
          j+=1
          if not cool: return False
        if j == len(s): return True
        return False
