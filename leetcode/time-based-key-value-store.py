# https://leetcode.com/problems/time-based-key-value-store/
from collections import defaultdict
from bisect import bisect_right, insort_right
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._values = defaultdict(list)
        self._data_for_timestamp = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        
        #i = bisect_right(self._values[key],timestamp)
        #if i >0 and i<=len(self._values[key]) and self._values[key][i-1] == timestamp:
        #    pass
        #else:
        self._values[key].append(timestamp)
        self._data_for_timestamp[(key, timestamp)] = value
            
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        i = bisect_right(self._values[key],timestamp)
        #print key, timestamp, self._values, self._data_for_timestamp, i
        
        if i >0 and i<=len(self._values[key]):
            return self._data_for_timestamp[(key, self._values[key][i-1])]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
