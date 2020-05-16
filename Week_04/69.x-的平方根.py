#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x // 2 + 1
        while left < right:
            mid = (left + right + 1) >> 1
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid

        return left
# @lc code=end

