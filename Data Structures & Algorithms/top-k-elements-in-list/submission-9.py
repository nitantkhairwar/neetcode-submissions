class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = Counter(nums)
        
        heap =[]
        res = []
        for key, val in dict1.items():
            heapq.heappush(heap, (-val, key))
            
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res