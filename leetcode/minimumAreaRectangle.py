# https://leetcode.com/problems/minimum-area-rectangle/description/
"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

from collections import defaultdict
class Solution:
    
    def minAreaRect(self, points):
         """
        :type points: List[List[int]]
        :rtype: int
        """
        same_x = defaultdict(lambda:set())
        same_y = defaultdict(lambda:set())
        for (x,y) in points:
            same_x[x].add((x,y))
            same_y[y].add((x,y))

        best_area = None
        for (x,y) in points:
            for same_x_point in same_x[x]:
                if same_x_point[1] < y:continue
                for same_y_point in same_y[y]:
                    if same_y_point[0] < x: continue

                    if (same_y_point[0], same_x_point[1]) in same_y[same_x_point[1]]:
                        area = abs(same_x_point[1] - y) * abs(same_y_point[0] - x)
                        if area > 0  and (best_area is None or best_area > area): best_area = area
        return 0 if best_area is None else best_area
                    
                
