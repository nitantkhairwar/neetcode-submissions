class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        for v in nums:
            heapq.heappush(self.minheap, v)
            if len(self.minheap) > k:
                heapq.heappop(self.minheap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

# 1,2,3,3 ->3,5,6,7,8
#     kth larget - 3 , 3, 3, 5, 6 

