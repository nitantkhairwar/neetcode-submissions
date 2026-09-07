class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(houses):
            prev, curr = 0, 0
            for num in houses:
                prev, curr = curr, max(prev+num, curr)
            return curr

        return max(helper(nums[:-1]), helper(nums[1:]))