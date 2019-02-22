# https://leetcode.com/problems/powerful-integers/
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        s = set()
        if x == 0 and y == 0: return [2]
        pows_x = self.genereate_powers(x,bound) if x > 1 else [1]
        for each in pows_x:
            pows_y = self.genereate_powers(y,bound) if y > 1 else [1]
            for each2 in pows_y:
                if each+each2 <= bound:
                    s.add(each+each2)
                else:
                    break
        return list(s)
        
        
    def genereate_powers(self, x, bound):
        i = 1
        while(i < bound):
            yield i
            i *= x
        
        
