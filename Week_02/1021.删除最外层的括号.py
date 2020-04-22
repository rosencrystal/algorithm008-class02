#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        res = ''
        for s in S:
            if s == '(':
                count += 1
                if count > 1:
                    res += '('
            elif s == ')':
                count -= 1
                if count >= 1:
                    res += ')'
                else:
                    count = 0  
        return res              

        
# @lc code=end

