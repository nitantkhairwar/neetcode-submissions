class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[[]]

        
        for num in nums:
            res += [lst + [num] for lst in res]
        return res

        # nums = [1, 2]
        # res = [[], 1, ]
        # sol = []
        # i = 0 , (backtrack[1], backtrack[2])=> [],
