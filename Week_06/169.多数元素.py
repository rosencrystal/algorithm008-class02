#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = Counter(nums)
        # print(num_dict)
        max = 0
        res = 0
        for k, v in num_dict.items():
            if v > max:
                max = v
                res = k
        return res



# if __name__ == '__main__':
#     a = Solution()
#     a.majorityElement([2,2,1,1,1,2,2])
# @lc code=end

