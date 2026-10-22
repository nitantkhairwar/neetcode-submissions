class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:

                total = nums[left]+ nums[right]+nums[i]

                if total == 0:
                    res.add((nums[left], nums[right], nums[i]))
                    left+=1
                    right-=1
                elif total < 0:
                    left +=1
                else:
                    right -=1
        return [list(triplets) for triplets in res]
