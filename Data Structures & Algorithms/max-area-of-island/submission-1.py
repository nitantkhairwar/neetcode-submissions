class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
            
        visit = set()

        rows = len(grid)
        cols = len(grid[0])

        heap = [0]

        def area(r,c):
            m_area = 0
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            m_area+=1

            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if (
                        r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == 1 and 
                        (r,c) not in visit):

                        m_area+=1
                        q.append((r,c))
                        visit.add((r,c))
            return m_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    a = area(r,c)
                    heapq.heappush(heap, -a)

        return -heap[0]


