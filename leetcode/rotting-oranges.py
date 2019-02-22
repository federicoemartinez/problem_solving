#https://leetcode.com/problems/rotting-oranges/
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        first_node_adj = []
        un_rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==2:
                    first_node_adj.append((i,j))
                elif grid[i][j] ==1:
                    un_rotten.add((i,j))
        days = 0
        current_queue = []
        queue = first_node_adj
        visited = set()
        def adj(i,j):
            res = []
            if i > 0 and grid[i-1][j] == 1:
                res.append((i-1,j))
            if j > 0 and grid[i][j-1] == 1:
                res.append((i,j-1))
            if i < len(grid)-1 and grid[i+1][j] == 1:
                res.append((i+1,j))
            if j < len(grid[0])-1 and grid[i][j+1] == 1:
                res.append((i,j+1))
            return res
        
        if len(un_rotten) == 0:
            return 0
        first = True
        while(queue):
            #print days,queue, visited
            
            current = queue.pop()
            if current not in visited:
                visited.add(current)
                i,j = current
                current_queue.extend([a for a in adj(i,j) if a not in visited])
            if len(queue) == 0:
                queue = [x for x in current_queue if x not in visited]
                current_queue = []
                if len(queue) > 0:
                    days+=1
        if len(un_rotten - visited) == 0:
            return days
        return -1
            
        
