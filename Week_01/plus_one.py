#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list) -> list:
        flag = 1
        res = []

        for i in range(len(digits)):
            num = digits.pop() + flag
            if num >= 10:
                flag = 1
                res.append(num%10)
            else:
                flag = 0
                res.append(num)

        if flag == 1:
            res.append(flag)

        res.reverse()
        return res
# @lc code=end

