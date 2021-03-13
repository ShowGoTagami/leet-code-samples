#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, mn = 0, prices and prices[0]
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                mx = max(mx,prices[i]-mn)
            else:
                mn = min(mn,prices[i])
        return mx
# @lc code=end

