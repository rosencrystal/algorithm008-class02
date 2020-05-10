学习笔记
# 1 搜索 - 遍历
在树（图、状态集合）中寻找特点的节点
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```
* 每个节点都要访问一遍，仅且访问一遍
* 对于节点的访问顺序分为dfs和bfs

## 1.1 深度优先搜索 DFS -> Depth First Search

* 二叉树
```
visited = set()

def dfs(node, visited):
    # terminator 
    if node in visited:
        # already visited
        return 
    visited.add(node)

    # process current node
    # ToDO ... logic here
    dfs(node.left)
    dfs(node.right)
```

* 多叉树
```
visited = set()

def dfs(node, visited):
    # terminator 
    if node in visited:
        # already visited
        return 
    visited.add(node)

    # process current node
    # ToDO ... logic here

    for next_node in node.children():
    if not next_node in visited:
        dfs(next_node, visited)
    
```

* 非递归写法：自己维护一个stack
```
def dfs(self, tree):
    if tree.root is None:
        return []

    visited, stack = [], [tree.root]    

    while stack:
        node = stack.pop()
        visited.append(node)

        process(node)

        nodes = generate_related_nodes(node)

        stack.push(nodes)

    # other processing work 
```

## 1.2 广度优先搜索 BFS -> Breadth First Search
```
def bfs(graph, start, end):


    visited, queue = [], [start]    

    while queue:
        node = queue.pop()
        visited.append(node)

        process(node)

        nodes = generate_related_nodes(node)

        queue.push(nodes)

    # other processing work 
```

# 2. 贪心算法
## 2.1 定义
贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

**每一步都是最优解，不一定全局是最优解！**

## 2.2 贪心和动态规划的区别

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。

一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

## 适用贪心算法的场景
简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。

# 3. 二分查找
## 3.1 二分查找的前提
* 目标函数单调性（单调递增或者递减，**当集合仅具有两种单调情况下也适用**） 
* 存在上下界（bounded）
* 能够通过索引访问（index accessible)

## 3.2 代码模板
```
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2  # mid =  (left + right) >> 1
        if array[mid] == target:    # find the target
            break or return result
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```

## 3.3 实例分析
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索数组中开始无序的地方。

如果数组已经有序返回-1

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2]
输出: 3，从7这里开始变得无序了，7的下标是3

输入: nums = [12,15,6,7,8,9,10]
输出: 1，从15这里开始变得无序了,15的下标是1

```
from typing import List


class Solution:
    def findDisorderIndex(self, nums: List[int]) -> int:
        # 如果给定的列表为空或只有一个元素，认为已经有序，直接返回-1
        if not nums or len(nums) < 2: return -1

        # 初始化二分查找边界
        left, right = 0, len(nums) - 1


        # 其他情况才进入循环
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1   # 使用位运算加速代码执行
            # 如果中间值比右边界大，无序点就在右侧
            # 如果mid比它的后一个大：
            #   1. 如果mid不是left的情况下：mid比它的前一个大，说明它就是转折点；mid比它的后一个大，但是比前一个小，说明转折点在这之前，把右边界设为mid - 1
            #   2. 如果mid已经和left重合，说明比较下来只有两个元素了，从第left起就无序了
            if nums[mid] > nums[right]:
                if nums[mid] > nums[mid + 1]:
                    if mid != left:
                        if nums[mid] > nums[mid - 1]:
                            return mid
                        else:
                            right = mid - 1
                    else:
                        return left        
                else:
                    left = mid
            # 如果中间值比右边界小说明右侧数据已经排序，只需要更新右边界就可以了      
            elif nums[mid] < nums[right]:
                if mid != left:
                    right = mid - 1
                else:
                    return left  

        # 全部查找完后返现都有序，返回-1
        return - 1    

if __name__ == '__main__':
    a = Solution()
    b = a.findDisorderIndex([1,2,3,4,5,6,7])
    print('result is %d' %b)
```