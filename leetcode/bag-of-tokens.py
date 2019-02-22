# https://leetcode.com/problems/bag-of-tokens/
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        points = 0
        max_points = 0
        while(tokens):
            if P >= tokens[0]:
                points+=1
                if max_points < points:
                    max_points = points
                P-=tokens[0]
                tokens.pop(0)
            else:
                if points > 0:
                    max_token = tokens.pop()
                    P+=max_token
                    points -=1
                else:
                    return max_points
        return max_points
