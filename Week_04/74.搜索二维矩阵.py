#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
# 
from typing import List


# @lc code=start
# 解法1：将矩阵拼接成一个数组，再二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        nums = []
        for m in matrix:
            nums += m

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return True if nums[left] == target else False   

# @lc code=end

