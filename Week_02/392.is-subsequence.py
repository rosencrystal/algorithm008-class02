#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 判断 s 是否为 t 的子序列。
    	b = iter(t)  # 迭代器
    	return all(((i in b) for i in s ))


# @lc code=end

