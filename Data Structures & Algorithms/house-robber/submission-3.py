class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        rob = [0]*n
        rob[0] = nums[0]
        if rob[0]> nums[1]:
            rob[1] = rob[0]
        else:
            rob[1] = nums[1]
        n = len(nums)
        for i in range(2,n):
            rob[i] = max(nums[i]+rob[i-2], rob[i-1])
        return max(rob)