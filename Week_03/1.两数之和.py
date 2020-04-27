#
# @lc app=leetcode.cn id=1 lang=python3
# 法一： 普通解法
# [1] 两数之和
# 1. 找出所有比target小的数，并将它们放在一个数组less_target中
# 2. 依次从上面的数组中去数字然后做减法得到一个val，然后判断该值能否在less_target中找到，如果能则得到一个结果并返回；如果不能则继续，直到所有的元素被遍历
# import sys

# @lc code=start
# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         for i, num in enumerate(nums):
#             val = target - num
#             try:
#                 i_val = nums.index(val, i+1)
#                 if i < i_val:
#                     return [i, i_val]
#                 continue
#             except ValueError:
#                 # print('not find %d', val)
#                 continue    
#         return []

# 法二：字典hash法
# 字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤
# @lc code=start
# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         hashmap={}
#         for ind,num in enumerate(nums):
#             hashmap[num] = ind
#         for i,num in enumerate(nums):
#             j = hashmap.get(target - num)
#             if j is not None and i!=j:
#                 return [i,j]


# 法三：优化的字典hash法
# 不需要 mun2 不需要在整个 dict 中去查找。可以在 num1 之前的 dict 中查找，因此就只需要一次循环可解决
# @lc code=start
# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         hashmap={}
#         for i,num in enumerate(nums):
#             if hashmap.get(target - num) is not None:
#                 return [i,hashmap.get(target - num)]
#             hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
# @lc code=start
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap.get(diff), i] # i应该放在后面的位置
            hashmap[value] = i # 如果hashmap中没有diff值, 则把value作为键/位置索引作为值赋给hashmap(注意位置别颠倒)


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

