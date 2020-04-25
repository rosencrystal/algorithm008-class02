#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: list) -> list:
        # arr.sort()
        # result = {}
        # diff_set = set()
        # for i in range(len(arr) -1):
        #     diff = abs(arr[i+1] - arr[i])
        #     if diff not in diff_set:
        #         diff_set.add(diff)
        #         result[str(diff)] = []    
        #     result[str(diff)].append(arr[i:i+2]) 
        # # print(arr)       
        # # print(diff_set)
        # # print(result)
        # sorted_key = [int(key) for key in list(result.keys())]
        # sorted_key.sort()
        # # print(sorted_key)
        # return result[str(sorted_key[0])]
        # -----------------------------------------
        arr.sort()
        sub_list = [(arr[i] - arr[i-1]) for i in range(1, len(arr))]
        min_sub = min(sub_list)
        result = []
        for t in range(len(sub_list)):
            if sub_list[t] == min_sub:
                result.append([arr[t], arr[t+1]])

        return result


if __name__ == '__main__':
    a = Solution()
    test = [3,8,-10,23,19,-4,-14,27]
    print(a.minimumAbsDifference(test))
        
# @lc code=end

