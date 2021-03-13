#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      for num in nums:
            ans = abs(num) - 1
            if nums[ans] > 0:
                nums[ans] *= -1
      return [i+1 for i in range(len(nums)) if nums[i] > 0]
# @lc code=end

