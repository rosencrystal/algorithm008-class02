#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack_r = set()
        stack_c = set()
        m = len(matrix[0])
        n = 0
        zero_list = [0 for i in range(m)]
        for i, row in enumerate(matrix):
            for j in range(m):
                if row[j] == 0:
                    stack_r.add(i)
                    stack_c.add(j)
            n = i + 1        

    
        for r in stack_r:
            matrix[r] = zero_list

        for c in stack_c:
            for i in range(n):
                matrix[i][c] = 0



# @lc code=end

