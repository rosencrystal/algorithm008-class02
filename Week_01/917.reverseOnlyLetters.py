#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
# 1. 得到仅包含字母的列表和一个保持原有其他字符的列表（该列表中）
# 2. 反转字符列表
# 3. 

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        chars = []
        tmp = []
        ret = []
        a = 0
        for s in S:
            print(ord(s))
            if 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122:
                chars.append(ord(s))
                tmp.append(32)
            else:
                tmp.append(ord(s))   
        # print(chars)
        # print(tmp)
        chars.reverse() 
        for t in tmp:
            if t == 32:
                ret.append(chr(chars[a]))
                a += 1
            else:
                ret.append(chr(t))    

        return ''.join(ret)

        
# @lc code=end

