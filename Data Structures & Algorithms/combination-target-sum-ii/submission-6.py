class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, sol = [], []
        n = len(nums)

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            if curr_sum > target or i == n:
                return

            # Choose nums[i]
            sol.append(nums[i])
            backtrack(i+1, curr_sum + nums[i])
            sol.pop()

            # Don't choose nums[i]
            idx = i+1
            while (
                idx < n and nums[idx] == nums[idx-1]):
                idx=idx+1
            backtrack(idx, curr_sum)

        backtrack(0, 0)
        return res