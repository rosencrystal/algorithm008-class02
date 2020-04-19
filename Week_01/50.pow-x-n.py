#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def re_binarysearch(x, n): # 逆向二分查找
            # 递归出口
            if n < 1:
                return 1
            count, sum = 1, x  # 初始化
            # 二分查找
            while count * 2 <= n:
                count += count  # 计数器翻倍
                sum *= sum  # 累乘
            return re_binarysearch(x, n-count) * sum  # 返回累乘结果
        
        res = re_binarysearch(abs(x), abs(n))  # 调用二分查找，传入绝对值
        # 符号处理
        res = -res if x < 0 and n % 2 != 0 else res
        res = 1/res if n < 0 else res
        return res

# @lc code=end

