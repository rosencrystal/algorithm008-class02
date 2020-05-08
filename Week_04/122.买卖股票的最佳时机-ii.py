#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        last = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > last:
                res += prices[i] - prices[i - 1]
                last = prices[i]
            elif prices[i] < last:
                last = prices[i]
        return res

# @lc code=end

