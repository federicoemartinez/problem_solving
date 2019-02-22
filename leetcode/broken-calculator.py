# https://leetcode.com/problems/broken-calculator/
class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        max_steps = None
        if X >= Y:
            max_steps = X - Y
            return max_steps
        else:
            Z = X
            max_steps = 0
            while(Z < Y):
                Z = 2 * Z
                max_steps +=1
            max_steps_aux = max_steps -1
            max_steps += Z - Y
            return self.brokenCalcAux(X,Y,max_steps, {})
            
            
        
    def brokenCalcAux(self, X, Y, steps, memo):
        #print X,Y, steps
        if Y ==0:
            return -1
        if Y in memo:
            return memo[Y]
        if X == Y:
            return 0
        if steps <= 0:
            return -1
        if X > Y:
            return X - Y
        else:
            if Y % 2 == 0 :
                aux_2 = self.brokenCalcAux(X, Y/2, steps-1, memo)
                if aux_2 != -1: aux_2 +=1
            else:
                aux_2 = self.brokenCalcAux(X, (Y+1)/2, steps-2, memo)
                if aux_2 != -1: aux_2 +=2
            if Y / 2 < X:
                acum = 0
                Y_ = Y
                while(Y_/2 < X):
                    Y_ += 1
                    acum+=1
                aux_1 = self.brokenCalcAux(X, Y_, steps-1, memo)
                if aux_1 != -1: aux_1 +=acum
            else:
                aux_1 = -1
            if aux_1 == -1 and aux_2 == -1: return -1
            memo[Y] = min([x for x in [aux_1,aux_2] if x > -1])
            return memo[Y]
            
