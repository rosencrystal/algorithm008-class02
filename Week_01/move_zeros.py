#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
# author: rosencrystal@163.com

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1