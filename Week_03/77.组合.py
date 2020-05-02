#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, n, k, [], res)
        return res

    def __dfs(self, start, end, k, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, end + 1):
            pre.append(i)
            self.__dfs(i + 1, end, k, pre, res)
            pre.pop()




# @lc code=end

