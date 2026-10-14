class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        
        for arr in points:
            arr1 = arr[0]
            arr2 = arr[1]
            dist = arr1**2 + arr2**2
            heapq.heappush(minheap, [-dist,arr1, arr2])

            if len(minheap) > k :
                heapq.heappop(minheap)
        return [[x,y] for _,x,y in minheap]