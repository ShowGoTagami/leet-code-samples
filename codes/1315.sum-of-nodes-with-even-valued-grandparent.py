#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(cur: TreeNode, par: TreeNode, gra: TreeNode):
          if gra and gra.val % 2 == 0:
            nonlocal ans
            ans += cur.val
          if cur.left:
            dfs(cur.left, cur, par)
          if cur.right:
            dfs(cur.right, cur, par)
        ans = 0
        dfs(root, None, None)
        return ans
# @lc code=end

