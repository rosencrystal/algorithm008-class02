#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A=0
        B_number=0
        for i,j in  zip(secret,guess):
            if i==j:
                A+=1
        B=dict()
        C=dict()
        for i in secret:
            if i in B:
                B[i]+=1
            else:
                B[i]=1
        for j in guess:
            if j in C:
                C[j]+=1
            else:
                C[j]=1
        for i in B.keys():
            if i in C.keys():
                B_number=min(B[i],C[i])+B_number
        B_number=B_number-A
        return str(A)+"A"+str(B_number)+"B"

# @lc code=end

