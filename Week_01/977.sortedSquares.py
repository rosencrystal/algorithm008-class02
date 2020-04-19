#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: list) -> list:
        rel = [i*i for i in A]
        rel.sort()
        return rel
        
# @lc code=end

