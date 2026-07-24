class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)
        left = 1
        for i in range(len(nums)):
            arr[i] = left
            left *= nums[i]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= right
            right *= nums[i]
        return arr
