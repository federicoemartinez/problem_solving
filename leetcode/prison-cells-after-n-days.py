# https://leetcode.com/problems/prison-cells-after-n-days/
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        i = 0
        d = {}
        cells = tuple(cells)
        
        while(i < N):
            row = []
            if cells in d:
                k = (N-i) / (i- d[cells][1])
                i += (i- d[cells][1]) * k 
                #cells = d[cells][0]
                if k == 0:
                    i+=1
                    cells = d[cells][0]
                continue
                
            for j in range(len(cells)):
                if j == 0 or j == len(cells)-1:
                    row.append(0)
                else:
                    if cells[j-1] == cells[j+1]:
                        row.append(1)
                    else:
                        row.append(0)
            tup = tuple(row)
            d[cells] = (tup, i)
            cells = tup
            i+=1
        return cells
                
        
