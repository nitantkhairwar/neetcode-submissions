class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        #dp1 
        prev1 = nums[0]
        curr1 = max(nums[0], nums[1])
        for i in range(2, n-1):
            curr1, prev1 = max(prev1+nums[i], curr1), curr1
        #dp2
        prev2 = 0
        curr2 = nums[1]
        for i in range(2, n):
            curr2, prev2 = max(prev2+nums[i], curr2), curr2

        return max(curr1, curr2)