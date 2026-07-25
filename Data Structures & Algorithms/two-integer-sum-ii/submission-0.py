class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        first = 0
        last = len(n)-1
        while(first != last):
            tsum = n[first] + n[last]
            if tsum == target:
                return [first+1,last+1]
            if tsum < target:
                first+=1
            if tsum > target:
                last-=1
            