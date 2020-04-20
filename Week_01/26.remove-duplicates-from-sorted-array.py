#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        for num_index in range(len(nums)-1, 0, -1):
            if nums[num_index] == nums[num_index-1]:
                nums.pop(num_index)
        return len(nums)

# @lc code=end

