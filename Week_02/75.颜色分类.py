#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 法一：三指针，把0往前放，2往后放，1不管
        # index用于保存之前1的位置，等找到0的时候再把0换过来
        index = left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                index += 1
                left += 1
            elif nums[left]  == 2:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
            else:
                left += 1    


# @lc code=end

