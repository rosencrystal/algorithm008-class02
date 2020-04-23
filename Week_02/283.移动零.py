#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         if i != j:
        #             nums[i] = 0
        #         j += 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i - count], nums[i] = nums[i], 0
            
# @lc code=end

