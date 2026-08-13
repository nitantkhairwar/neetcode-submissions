class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        m = []
        for i in stones:
            heapq.heappush(m , -i)
        while len(m)>1:
            f = -heapq.heappop(m)
            s = -heapq.heappop(m)
            if  f > s :
                heapq.heappush(m, -(f-s))
            elif s > f:
                heapq.heappush(m, -(s-f))
        return -m[0] if len(m) else 0
                

