#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        
        temp = s.strip().split(' ')
        # print(temp)
        count = 0
        for i in range(len(temp)):
            if temp[i]:
                while ' ' in temp[i]:
                    temp[i] = temp[i].strip()
                    if not temp[i]:
                        count += 1
            else:
                count += 1

        return len(temp) - count

        

# a = Solution()        
# b = "                "
# c = a.countSegments(b)
# @lc code=end

