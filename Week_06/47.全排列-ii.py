#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
from typing import List
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        res = []    
        visted = [False] * len(nums)
        nums.sort()

        def dfs(numbers, result, current, visted):
            if len(current) == len(numbers):
                result.append(current[:])
                return

            for i in range(len(numbers)):
                if visted[i] or i > 0 and numbers[i] == numbers[i - 1] and not visted[i - 1]:
                    continue
                
                current.append(numbers[i])
                visted[i] = True
                dfs(numbers, result, current, visted)
                current.pop()
                visted[i] = False

        dfs(nums, res, [], visted)
        return res



# @lc code=end

