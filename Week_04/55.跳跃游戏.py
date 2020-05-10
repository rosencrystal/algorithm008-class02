#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return True

        res = False
        least_step = 1
        last = False
        nums.reverse()
        for i in range(1, len(nums)):
            flag = nums[i] >= 1 and last
            if nums[i] >= least_step or flag:
                last = True
                least_step = 1
                if i == len(nums) - 1:
                    res = True
            else:
                last = False
                least_step += 1
        return res

# @lc code=end

