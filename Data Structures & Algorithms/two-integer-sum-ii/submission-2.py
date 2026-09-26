class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers)-1
        while first != last:
            tsum = numbers[last]+numbers[first]
            if tsum == target:
                return [first+1, last+1]
            elif tsum > target:
                last-=1
            elif tsum < target:
                first+=1
        return []