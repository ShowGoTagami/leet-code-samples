#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)-1):
          verticalDiff = abs(points[i][0] - points[i+1][0])
          horizontalDiff = abs(points[i][1] - points[i+1][1])
          count += max(verticalDiff, horizontalDiff)
        return count
# @lc code=end

