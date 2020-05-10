#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
from typing import List
from collections import defaultdict, deque


# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or len(wordList[0]) == 0: return []

        res = []
        size, general_dic = len(wordList[0]), defaultdict(list)
        # 构建邻接关系桶
        # 将所有单词构建桶，便于查找邻接词。构建桶的方式是依次将一个词的各个字母挖空，用字典进行保存
        for word in wordList:
            for i in range(size):
                general_dic[word[:i] + '*' + word[i+1:]].append(word)

        # print(general_dic)
        # BFS
        # 广度队列
        queue = deque()                 # 前溯词队列
        queue.append((beginWord, 1))    # 待遍历此及其深度
        beFound = {beginWord: 1}        # 已探测词的列表
        # 用一个默认列表字典记录到达该节点的前溯词列表，这里需注意对于每个可能搜索到该词的路径
        # 只要深度不超过已有路径，都应加入前溯词列表
        preWords = defaultdict(list)    # 前溯词列表
        while queue:
            # print('current queue:')
            # print(queue)
            cur_word, level = queue.popleft()
            for j in range(size):
                for neighbour in general_dic[cur_word[:j] + '*' + cur_word[j+1:]]:
                    if neighbour not in beFound:
                        beFound[neighbour] = level + 1
                        queue.append((neighbour, level + 1))  
                    if beFound[neighbour] == level + 1:
                        preWords[neighbour].append(cur_word)
            # 已搜索到目标词，且完成当前层遍历           
            if endWord in beFound and level + 1 > beFound[endWord]:
                break

        # print(preWords)
        # 列表推导式输出结果
        if endWord in beFound:
            res = [[endWord]]  
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in preWords[r[0]]]
        return res                 


# if __name__ == '__main__':
#     a = Solution()
#     beginWord = "hit"
#     endWord = "cog"
#     wordList = ["hot","dot","dog","lot","log","cog"]
#     b = a.findLadders(beginWord, endWord, wordList)
#     print(b)

# @lc code=end

