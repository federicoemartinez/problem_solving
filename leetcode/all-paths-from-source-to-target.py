# https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.all_paths(0,graph,{len(graph)-1:[[len(graph)-1]]})
        
        
    def all_paths(self, node, graph,memo):
  
        if node in memo:
            return memo[node]
        res = []
        for each in graph[node]:
            l = self.all_paths(each, graph,memo)
            res.extend(([node]+x for x in l))
        memo[node] = res
        return res
            
        
