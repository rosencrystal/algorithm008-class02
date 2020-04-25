#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
# 方法一： 使用Counter类
# Counter 是一个在collections包里的类，正如其名，是一个用于计数的工具。
# 我们可以用Counter(nums)这样的构造函数构造一个Counter类，其中nums是一个列表。
# 构造好的Counter实例可以看作一个字典，键是nums的每一项，值是它的出现次数。
# 举个例子:
# 如果一个列表a = [1,1,3,4,3]，你想要统计每项的出现次数，那么你使用b = Counter(a)，那么这时候b就像一个这样的字典{1:2,3:2,4:1}，表示数字1出现了2次，数字3出现了2次，数字4出现了1次。
# 可是题目里要我们输出的是最多的K项
# 这时候可以应用Counter的一个函数，most_common(k)
# 这个函数就是返回最多出现的K项
# 但是返回的形式是一个元祖列表，类似[(1,2),(3,2),(4,1)]的形式
# 我们只需要键也就是第一项，所以要使用列表生成式处理一下即可。


# from collections import Counter
# # @lc code=start
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         return [ct[0] for ct in Counter(nums).most_common(k)]       


# ----------------------------------------------------------------------------
# 方法二：使用堆排序
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        思路：先统计每个字符的频率, 维护一个大小为k的小顶堆。堆顶是元素频率最小的（频率，元素）对，
        如果发现新加入（频率，元素）对，其频率比堆顶的大，则弹出堆顶元素，然后插入新的元素。最后遍历完
        所有元素，堆中就是频率最高的k个元素。程序的时间复杂度是 O(nlogk)
        """
        if not nums or len(nums) == 1:
            return nums
        freq_dict = collections.Counter(nums)
        # print(freq_dict)
        priority_queue = []
        # 扫描freq，维护当前出现频率最高的k个元素，优先队列（堆）中存放元组（频率，元素）
        for element, freq in freq_dict.items():
            if len(priority_queue) == k:
                if freq > priority_queue[0][0]: # 新加入的元素频率比堆中最小频率要大
                    heapq.heappop(priority_queue) # 弹出堆顶元素
                    heapq.heappush(priority_queue, (freq, element))
            else:
                 heapq.heappush(priority_queue, (freq, element))
            # print(priority_queue)

        return [item[1] for item in priority_queue]


# @lc code=end

