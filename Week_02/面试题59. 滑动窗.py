class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = []
        if len(nums) > 0:
            window = nums[0:k]
            result.append(max(window))
            for i in range(k, len(nums)):
                window.pop(0)
                window.append(nums[i])
                result.append(max(window))
        return result