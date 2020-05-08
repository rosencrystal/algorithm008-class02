#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
from typing import List
import collections


# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankset = set(bank)
        ls = list(start)
        visited = set()
        queue = collections.deque()
        queue.append(ls)
        visited.add(start)
        cand = ['A','C', 'G', 'T']
        level = 0
        while queue:
            for _ in range(len(queue)):
                ls = queue.popleft()
                if ''.join(ls) == end:
                    return level
                for i, v in enumerate(ls):
                    for c in cand:
                        ls[i] = c
                        cur = ''.join(ls)
                        if cur not in visited and cur in bankset:
                            queue.append(ls[:])
                            visited.add(cur)
                    ls[i] = v
            level += 1
        return -1

        
# @lc code=end

