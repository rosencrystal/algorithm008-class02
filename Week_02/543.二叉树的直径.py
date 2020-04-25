#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)

        return self.max

    def depth(self, root):
        if not root:
            return 0
        dl = self.depth(root.left)    
        dr = self.depth(root.right)
        self.max = max(self.max, dl + dr)

        return max(dl, dr) + 1
        
# @lc code=end

