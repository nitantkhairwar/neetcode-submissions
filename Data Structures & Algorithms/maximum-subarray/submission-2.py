class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float("-inf")
        n = len(nums)-1
        curr = 0
        for num in nums:
            curr+= num
            maximum = max(maximum, curr)
            if curr < 0:
                curr = 0
        return maximum