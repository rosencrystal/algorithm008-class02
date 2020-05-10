#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# 解法：转换为图，BFS
# 1. 这道题对 检查两个单词是否是相邻的，复杂度要求很高。我们需要在很快的速度上判定，是否有可用的相邻节点
# 2. 需要将问题抽象化成为图论问题。
# 函数：defaultdict( type )
# 其传入参数必须是type, 例如 int, list, set等，而返回的默认值，就是这些type下的默认值，例如int返回的默认值是0，list是空list等

# defaultdict与普通dict的最大作用在于：
# 你可以直接call一个不存在的key， 如果不存在这个key，那就先直接创建这个key，并根据默认值的设置，赋值value，而后在继续操作。
# 省去了
# dict[new] = dict.get(new, default = [])
# 然后才能使用dict[new]来进一步操作。
# 相比之下：你可放心大胆的用：defaultdict[new] 管他有没有。
# for 找head
#     while queue：
#         for 找邻居
#             if 没有重复：处理，标记，入队

# 如何mark
# mark的方法有很多，常见的方法是把所有遍历过的node放到set里，每次都去set里查看，是否已经存在于set里了。
# 也可以写一个dict，key是node，value是bool，表示是否访问过了

# 如何找邻居
# 在这道题中，找邻居的方法比较复杂：

# for 所有可能去掉一个字母的同源
#     for 每个同源的都是邻居
            
# https://leetcode-cn.com/problems/word-ladder/solution/python-shen-du-jiang-jie-bfsde-jie-gou-by-allen-23/
from typing import List
from collections import defaultdict, deque


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 建立通用list
        size, general_dic = len(beginWord), defaultdict(list)
        for word in wordList:
            # print('current word is %s' % word)
            for _ in range(size):
                # print('current key is %s' % word[:_] + '*' + word[_+1:])
                general_dic[word[:_] + '*' + word[_+1:]].append(word)

        # print(general_dic)
        # BFS
        queue = deque() 
        # 因为在BFS中，queue中通常会同时混合多层的node，这就无法区分层了
        # 要区分层就要queue中直接加入当前node所属层数       
        queue.append((beginWord, 1))
        mark_dic = defaultdict(bool)
        mark_dic[beginWord] = True

        while queue:
            # print('current queue:')
            # print(queue)
            # queue从头pop一个出来
            curr_word, level = queue.popleft()
            # 找邻居，这里的所有邻居都在level+1层
            for i in range(size):
                # print(general_dic[curr_word[:i] + '*' + curr_word[i+1:]])
                for neighbour in general_dic[curr_word[:i] + '*' + curr_word[i+1:]]:
                    # print('looking neighbour: %s' % neighbour)
                    if neighbour == endWord: return level + 1
                    # 符合条件（neighbour + unmarked)的进去
                    if not mark_dic[neighbour]:
                        # print('found a valid neighbour: %s' % neighbour)
                        mark_dic[neighbour] = True
                        queue.append((neighbour, level + 1))

        return 0                

# if __name__ == '__main__':
#     a = Solution()
#     beginWord = "hit"
#     endWord = "cog"
#     wordList = ["hot","dot","dog","lot","log","cog"]
#     b = a.ladderLength(beginWord, endWord, wordList)
#     print('result is %d' % b)
        
# @lc code=end

