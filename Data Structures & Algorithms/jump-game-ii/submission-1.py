class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        destination = n-1
        last_idx = 0
        coverage = 0

        jumps = 0

        if n == 1:
            return 0

        for i in range(n):
            coverage = max(coverage, i+nums[i])

            if  i == last_idx :

                last_idx = coverage
                jumps+=1

                if coverage >= destination :
                    return jumps
        return None