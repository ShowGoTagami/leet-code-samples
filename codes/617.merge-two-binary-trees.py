#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
          return root2
        if not root2:
          return root1
        ans = TreeNode(root1.val + root2.val)
        ans.left = self.mergeTrees(root1.left, root2.left)
        ans.right = self.mergeTrees(root1.right, root2.right)
        return ans
# @lc code=end
