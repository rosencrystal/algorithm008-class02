#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
# 法一： 数学归纳法

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         x, y = 0, 1
#         for i in range(n):
#             x, y = y, x + y

#         return y  


# 法二： 递推公式 num_list[i] = num_list[i-1] + num_list[i-2]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        num_list = [0]*(n+1)
        num_list[1] = 1
        num_list[2] = 2
        for i in range(3, n + 1):
            num_list[i] = num_list[i - 1] + num_list[i - 2]

        return num_list[-1]  
# @lc code=end

