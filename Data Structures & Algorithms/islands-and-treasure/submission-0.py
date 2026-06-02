from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
    
        q = deque()
        # Collect all treasure chests first
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        # Perform a single Multi-Source BFS
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # If the neighbor is a land cell and we found a shorter path
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))