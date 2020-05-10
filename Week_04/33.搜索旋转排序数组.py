#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        left, right = 0, len(nums) - 1
        mid = round(right / 2)

        if target == nums[left]: return left
        if target == nums[right]: return right

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            # print('left: %d, right: %d, mid: %d' % (left, right, mid))
            if target == nums[mid]: return mid

            if nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid
                else:
                    left = mid + 1

        return left if nums[left] == target else - 1    

# if __name__ == '__main__':
#     a = Solution()
#     b = a.search([4,5,6,7,0,1,2], 0)
#     print('result is %d' %b)

# @lc code=end

