#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
          return 0
        queue = deque([(root, 1)])
        while queue:
          curr, val = queue.popleft()
          if not curr.left and not curr.right and not queue:
                return val
          if curr.left:
              queue.append((curr.left, val+1))
          if curr.right:
              queue.append((curr.right, val+1))
# @lc code=end

