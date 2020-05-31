#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from typing import List

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 经典动态规划题, 初看例子好像可以贪心, 但是稍微换个更大的数就不行了
        # 换一个思路, 从后往前找
        # 前一层的每个元素对应下一层的两个元素,取其中小的相加
        res = triangle[-1]

        for i in range(len(triangle) - 2, -1, -1):      # i 是当前层, 从倒数第二层开始到第0层
            for j in range(len(triangle[i])):           # 遍历当前层的元素
                res[j] = min(res[j], res[j+1]) + triangle[i][j]

        return res[0]
        

        

        
# @lc code=end

