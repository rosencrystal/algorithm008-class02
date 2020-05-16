#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List


# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children, cookie = 0, 0
        n, m = len(g), len(s)
        if n == 0 or m ==0:
            return 0
        
        g.sort()
        s.sort()
        while children < n and cookie < m:
            if g[children] <= s[cookie]:
                children += 1
            cookie += 1

        return children


# @lc code=end

