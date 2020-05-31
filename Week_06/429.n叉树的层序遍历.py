#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#
from typing import List

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        level = 0

        def ntree(root, level):
            if not root: return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            for child in root.children:
                ntree(child, level+1)

        ntree(root, level)
        return res

# @lc code=end

