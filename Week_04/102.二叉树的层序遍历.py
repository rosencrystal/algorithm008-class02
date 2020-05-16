#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
from typing import List
from collections import deque, defaultdict


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        res = []
        queue = deque()
        queue.append((root, 0))
        general_dic = defaultdict(list)

        while queue:
            node, level = queue.popleft()
            general_dic[level].append(node.val)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        res = [v for v in general_dic.values()]
        return res



# @lc code=end

