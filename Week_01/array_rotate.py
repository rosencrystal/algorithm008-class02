#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i] #recycle

        for i in range(len(nums)):
            nums[i] = a[i]


# @lc code=end

