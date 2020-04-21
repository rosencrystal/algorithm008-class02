#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): 
            return self.intersect(nums2, nums1)
        hash = {}
        for num in nums1:
            if num not in hash:
                hash[num] = 1
            else: 
                hash[num] += 1

        res = []
        for num2 in nums2:
            if num2 in hash and hash[num2] > 0:
                res.append(num2)
                hash[num2] -= 1
        return res



# @lc code=end

