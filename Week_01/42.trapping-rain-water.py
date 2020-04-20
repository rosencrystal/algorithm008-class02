#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        res, idx = 0, 0
        stack = []
        while idx < n:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += h * dist
            stack.append(idx)
            idx += 1
        return res

# @lc code=end

