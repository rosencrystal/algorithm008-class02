#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 法一：优先队列（Heap）
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # if not lists or len(lists) == 0:
        #     return None
        # import heapq
        # heap = []
        # # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        # for node in lists:
        #     while node:
        #         heapq.heappush(heap, node.val)
        #         node = node.next
        # dummy = ListNode(None)
        # cur = dummy
        # # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        # while heap:
        #     temp_node = ListNode(heappop(heap))
        #     cur.next = temp_node
        #     cur = temp_node
        # return dummy.next

    # 法二：分治法
    def merge(self, node_a, node_b):
        dummy = ListNode(None)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:  # 对两个节点的 val 进行判断，直到一方的 next 为空
            if cursor_a.val <= cursor_b.val:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        # 有一方的next的为空，就没有比较的必要了，直接把不空的一边加入到结果的 next 上
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next = cursor_b
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)

        # 边界情况
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        # 分治
        mid = length // 2
        return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))


# @lc code=end

