#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List

# 法一：递归
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) <= 1:  # 递归终止条件
#             return [nums]
#         res = []
#         for idx, num in enumerate(nums):
#             res_nums = nums[:idx] + nums[idx + 1:]  # 确定剩余元素
#             for j in self.permute(res_nums):  
#                 res.append([num] + j)
#         return res

# 法二：回溯
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:  # 特殊情况处理
            return [nums]
        res = []
        visited = [False] * len(nums)

        def dfs(numbers, result, current, visit):
            if len(current) == len(numbers):    # 递归终止条件
                result.append(current[:])       # 要用[:]或copy

            for i in range(len(numbers)):
                if visit[i]:    # 如果访问过第i个元素，直接跳过
                    continue
                current.append(numbers[i])
                visit[i] = True
                dfs(numbers, result, current, visit)    # drill down
                # 回溯之前恢复到之前的状态
                current.pop()
                visit[i] = False

        dfs(nums, res, [], visited)        
        return res
# @lc code=end

