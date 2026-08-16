class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = collections.deque()
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        rows = len(grid)
        cols = len(grid[0])

        # Put all treasures into the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        # BFS
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 2147483647
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))