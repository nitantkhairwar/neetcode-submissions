class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        prev = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2,n):
            curr, prev = max(nums[i]+prev, curr), curr
        return curr