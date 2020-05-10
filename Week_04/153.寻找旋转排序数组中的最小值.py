#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
from typing import List


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # res = nums[0]
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if  nums[left] < nums[right]:
                if nums[left] <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid
            else:
                if nums[right] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid       
        return nums[left]

# @lc code=end

