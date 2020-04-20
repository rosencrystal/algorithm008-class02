#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
# 1. 找出所有比target小的数，并将它们放在一个数组less_target中
# 2. 依次从上面的数组中去数字然后做减法得到一个val，然后判断该值能否在less_target中找到，如果能则得到一个结果并返回；如果不能则继续，直到所有的元素被遍历
# import sys

# @lc code=start
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i, num in enumerate(nums):
            val = target - num
            try:
                i_val = nums.index(val, i+1)
                if i < i_val:
                    return [i, i_val]
                continue
            except ValueError:
                # print('not find %d', val)
                continue    
        return []


# if __name__ == '__main__':
#     # target = 9
#     # sys.stdout.write('nums = \n')
#     line = sys.stdin.readline()[1:-2].split(',')
#     # print(line)
#     nums = [int(l) for l in line]
#     # print(nums)
#     # sys.stdout.write('target = \n')
#     target = int(sys.stdin.readline().split('\n')[0])
#     s = Solution()
#     print(s.twoSum(nums, target))

# @lc code=end

