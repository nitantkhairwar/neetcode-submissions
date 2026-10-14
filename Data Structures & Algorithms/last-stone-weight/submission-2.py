class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for val in stones:
            heapq.heappush(maxheap, -val)

        while len(maxheap)> 1:
            first = -heapq.heappop(maxheap)
            second = -heapq.heappop(maxheap)

            if first > second:
                val = first - second
                heapq.heappush(maxheap, -val)
            
        return -maxheap[0] if len(maxheap) else 0

        