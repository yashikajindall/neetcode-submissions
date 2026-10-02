class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        best  = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue = deque([(r,c)]) 
                    grid[r][c] = 0
                    area  = 1

                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                area += 1
                                grid[nr][nc] = 0
                                queue.append((nr,nc))
                    best = max (area, best)
        return best 

        