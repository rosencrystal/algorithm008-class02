#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        cur_max = nums[0]       # 从原点开始可以跳的最远距离
        end = nums[0]           # 记录用最少的步数可以跳多远
        res = 1                 # 用于返回结果，数组长度至少为2，所以最少要跳1步

        # 如果第一步就可以跳到末尾，直接返回不进入循环
        if end >= len(nums) - 1: return res

        for i in range(1, len(nums)):
            cur_max = max(cur_max, i + nums[i]) # 更新最远可以到达的位置
            if i == end:                        #　如果ｉ走到了上次跳跃可达到的最远距离
                if end < len(nums) - 1:         # 如果这个end还没到达末尾,就跳一步，同时更新res和end
                    res += 1
                    end = cur_max
                    if end > len(nums) - 1:     # 更新完后立即判断和末尾的关系, 如果够了立即返回
                        return res
                else:                           # 说明已经走到末尾了,直接返回
                    return res
  

# @lc code=end

