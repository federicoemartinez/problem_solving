
# https://leetcode.com/problems/partition-labels/
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        s = S
        last_time = {}
        for i in xrange(len(S)):
            last_time[S[i]] = i
        i = 0
        res = []
        last_index_for_partition = i
        last_partition_start = 0
        N = len(s)
        while(i < N):
            last_index_for_partition = max(last_index_for_partition, last_time[S[i]])
            if i == last_index_for_partition:
                    res.append(i-last_partition_start+1)
                    last_partition_start = i+1
            i+=1
            
        return res
        
