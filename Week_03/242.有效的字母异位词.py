#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
# 法一：直接对两个字符串进行排序，然后比较是否相等
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# 法二：hash表法
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)       
        for k, v in count_s.items():
            if k in count_t.keys():
                if count_t[k] == v:
                    continue
                else:
                    return False
            else:
                  return False
        return True                

# @lc code=end

