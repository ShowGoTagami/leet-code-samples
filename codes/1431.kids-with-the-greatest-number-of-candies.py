#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        outputList = []
        for i in range(len(candies)):
          if (candies[i] + extraCandies) >= greatest:
            outputList.append(True)
          else:
            outputList.append(False)
        return outputList
# @lc code=end

