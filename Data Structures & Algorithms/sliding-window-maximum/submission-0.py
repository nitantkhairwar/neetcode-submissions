class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res =[]
        heap = []

        for i in range(k):
            heap.append((nums[i], i))
        
        heapq.heapify_max(heap)

        res.append(heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))

            window_start = i - k + 1
            while heap[0][1]< window_start:
                heapq.heappop_max(heap)

            res.append(heap[0][0])
        return res
