class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        final_position = n-1
        for i in range(n-2, -1,-1):
            if i+nums[i] >= final_position:
                final_position = i
        return final_position == 0

