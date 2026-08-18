class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return []

        atl= collections.deque()
        pac = collections.deque()
        a_seen = set()
        p_seen = set()
        r = len(heights)
        c = len(heights[0])

        for i in range(c):
            pac.append((0, i))
            p_seen.add((0, i))

        for i in range(1,r):
            pac.append((i, 0))
            p_seen.add((i, 0))

        for i in range(c):
            atl.append((r-1, i))
            a_seen.add((r-1, i))

        for i in range(0,r-1):
            atl.append((i, c-1))
            a_seen.add((i, c-1))

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def overlap(que, seen):
            while que:
                r1,c1 = que.popleft()
                for dr, dc in directions:
                    nr, nc = r1+dr, c1+dc
                    if (
                        nr in range(r) and nc in range(c) and 
                        heights[nr][nc] >= heights[r1][c1] and 
                        (nr,nc) not in seen):
                        seen.add((nr,nc))
                        que.append((nr,nc))
        
        overlap(atl, a_seen)
        overlap(pac, p_seen)
        result = list(a_seen.intersection(p_seen))

        return result