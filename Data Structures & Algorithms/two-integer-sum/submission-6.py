class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for i in range(n):
            num = target-nums[i]
            if num in seen:
                return[seen[num], i]
            seen[nums[i]]= i
        return []