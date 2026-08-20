class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n :
                res.append(sol[:])
                return
            
            #Choose the number
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #Don't choose the number
            idx = i+1
            while idx < n and nums[idx] == nums[idx-1]:
                idx+=1
            backtrack(idx)
        
        backtrack(0)
        return res