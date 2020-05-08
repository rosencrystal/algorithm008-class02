#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List


# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child, cookie = 0, 0
        m, n = len(g), len(s)
        if m == 0 or m == 0:
            return 0
        
        g.sort()
        s.sort()
        while child < m and cookie < n:
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        
        return child


# @lc code=end

