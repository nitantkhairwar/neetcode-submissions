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

            # Don't choose nums[i]
            # Skip all duplicates of nums[i]
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1

            backtrack(j, curr_sum)

            # Choose nums[i]
            sol.append(nums[i])
            backtrack(i + 1, curr_sum + nums[i])
            sol.pop()

        backtrack(0, 0)
        return res