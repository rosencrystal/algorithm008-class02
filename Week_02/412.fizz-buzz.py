#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [""] * n
        hash_map = {3:"Fizz", 5:"Buzz"}
        for i in range(n):
            for key in hash_map.keys():
                if (i + 1) % key == 0:
                    result[i] += hash_map[key]
            if result[i] == "":
                result[i] += str(i + 1)
        return result
 
        
# @lc code=end

