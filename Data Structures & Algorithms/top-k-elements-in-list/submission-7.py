class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0)+1
        
        heap =[]
        for key, val in dict1.items():
            heapq.heappush(heap, [val, key])
            if len(heap)>k:
                heapq.heappop(heap)
        return [key for freq,key in heap]
        