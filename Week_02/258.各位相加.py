#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # 法一：递推公式
        # return (num-1)%9+1 if num!=0 else 0

        # 法二：将各位拆成字符串，然后一个一个加，直到满足条件
        # while num >= 10:
        #     digit = list(map(int, str(num)))
        #     #因为我不想再用一个变量接结果我就把num先置零，以防历史值影响计算
        #     num = 0
        #     for i in range(len(digit)):
        #         num += digit[i]
        # return num

        # 法三：模10取位
        while num >= 10:
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            num = sum
        return num

            

# @lc code=end

