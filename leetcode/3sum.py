# https://leetcode.com/problems/3sum/description/
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from collections import defaultdict
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_dict = defaultdict(lambda: 0)
        for each in nums:
            nums_dict[each] +=1
        sol = set()
        lenght = len(nums)
        used_i = set()
        for i in range(lenght):
            if nums[i] in used_i:
                continue
            used_j = set()
            for j in range(i+1, lenght):
                if nums[j] in used_j: continue
                k = -1*(nums[i] + nums[j])
                if ( k in nums_dict and nums_dict[k] > ((1 if nums[j] == k else 0) + (1 if nums[i] == k else 0))):
                        l = [nums[i],nums[j],k]
                        l.sort()
                        sol.add(tuple(l))
                        used_i.add(nums[i])
                        used_j.add(nums[j])
        return [list(x) for x in sol]
