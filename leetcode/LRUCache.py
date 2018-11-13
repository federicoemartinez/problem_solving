https://leetcode.com/problems/lru-cache/description/
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""



class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.value = value
            self.key = key
            self.next = None
            self.prev = None
        
        
        def set_next(self, n):
            self.next = n
            
        def set_prev(self, n):
            self.prev = n
    
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_by_key = {}
        self.counter = 0
        self.first = None
        self.last = None

     
    

    def get(self, key):

        ret = self.node_by_key.get(key, None)
        if ret:
            self.put(key, ret.value)
            return ret.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.node_by_key:
            node = self.node_by_key[key]
            node.value = value
            if node.key == self.first.key: 
                return
            prev = node.prev
            if(prev):
                node.prev.next = node.next
            nextn = node.next
            if(nextn):
                nextn.prev = prev
            elif prev is None:
                self.last = node
            else:
                self.last = prev
            node.prev = None
            node.next = self.first
            self.first.prev = node
            self.first = node
        else:
            if self.counter < self.capacity:
                self.counter += 1
            else:
                to_remove = self.last
                self.last = to_remove.prev
                if(self.last):
                    self.last.next = None
                del self.node_by_key[to_remove.key]
                self.counter-=1
                return self.put(key,value)
            node = LRUCache.Node(key, value)
            if(not (self.first is None)):
                self.first.set_prev(node)
            if(self.last is None):
                self.last = node

            old_first = self.first
            self.first = None
            node.set_next(old_first)
            self.first = node
            self.node_by_key[key] = node
            
                
                

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
