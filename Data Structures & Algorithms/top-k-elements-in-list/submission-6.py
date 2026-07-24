class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, [value, key])
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [key for freq,key in heap]