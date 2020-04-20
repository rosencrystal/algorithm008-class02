#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(str.split(" ")) != len(list(pattern)):
            return False
        for l in zip(*set(zip(list(pattern), str.split(" ")))):
            if len(l) != len(set(l)):
                return False
        return True
        
# @lc code=end

