#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1] * n
        idx2, idx3, idx5 = 0, 0, 0
        for i in range(1, n):
            res[i] = min(res[idx2]*2, res[idx3]*3, res[idx5]*5)
            if res[i] == res[idx2]*2: idx2 += 1
            if res[i] == res[idx3]*3: idx3 += 1
            if res[i] == res[idx5]*5: idx5 += 1
        return res[n-1]


# @lc code=end

