# https://leetcode.com/problems/merge-k-sorted-lists/
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        if(lists):
            while(len(lists) > 1):
                new_lists = []
                while (lists):
                      list1 = lists.pop()
                      list2 = lists.pop() if lists else None
                      new_lists.append(self.mergetTwoLists(list1,list2))
                lists = new_lists
            return lists[0]
        return []
        
    def mergetTwoLists(self, list1, list2):
        first_node = None
        current_node = None
        current_list1 = list1
        current_list2 = list2
        while(current_list1 is not None and current_list2 is not None):
            if current_list1.val <= current_list2.val:
                new_node = ListNode(current_list1.val)
                current_list1 = current_list1.next
            else:
                new_node = ListNode(current_list2.val)
                current_list2 = current_list2.next
            if current_node is None:
                first_node = new_node
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node
                
        while(current_list1 is not None):
            new_node = ListNode(current_list1.val)
            current_list1 = current_list1.next
            if current_node is None:
                first_node = new_node
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node
        while(current_list2 is not None):
            new_node = ListNode(current_list2.val)
            current_list2 = current_list2.next
            if current_node is None:
                first_node = new_node
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node
        return first_node
