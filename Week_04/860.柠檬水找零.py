#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#
from typing import List


# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        lq = {5:0, 10: 0}
        for bl in bills:
            if bl == 5:
                lq[5] += 1
            elif bl == 10:
                lq[10] += 1
                if lq[5] > 0:
                    lq[5] -= 1
                else:
                    return False
            else:
                if lq[10] > 0 and lq[5] > 0:
                    lq[5] -= 1
                    lq[10] -= 1
                elif lq[5] >= 3:
                    lq[5] -= 3
                else:
                    return False
        return True


        
# @lc code=end

