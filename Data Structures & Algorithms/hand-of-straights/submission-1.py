class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0]
            for num in range(start, start+groupSize):
                if num not in heap:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    heapq.heappop(heap)
        return True