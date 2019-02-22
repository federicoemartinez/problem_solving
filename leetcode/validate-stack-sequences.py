# https://leetcode.com/problems/validate-stack-sequences/
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        current_stack = []
        i = 0
        j = 0
        while(i < len(pushed) and j < len(popped)):
            if len(current_stack) > 0:
                if current_stack[-1] == popped[j]:
                    current_stack.pop()
                    j+=1
                else:
                    current_stack.append(pushed[i])
                    i+=1
            else:
                current_stack.append(pushed[i])
                i+=1
        if i==len(pushed) and j < len(popped):
            while(j < len(popped)):
                if current_stack[-1] == popped[j]:
                    current_stack.pop()
                    j+=1
                else:
                    return False
        return True
                
            
