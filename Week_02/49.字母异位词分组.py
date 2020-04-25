#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res =[]
        for word in strs:
            dic.setdefault(str(sorted(word)),[]).append(word)
        for value in dic.values():
            res.append(value)
        return res


# @lc code=end

