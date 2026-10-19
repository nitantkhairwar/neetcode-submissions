class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        final = n-1

        for i in range(n-2,-1, -1):
            if i+nums[i] >= final:
                final = i
        return final == 0