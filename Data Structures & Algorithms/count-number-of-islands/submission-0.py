class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start dfs from "1", when visit mark this as "0"
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j >= cols or j < 0 or grid[i][j] == "0":
                return 
            
            grid[i][j] = "0"
            for dx, dy in dirs:
                dfs(i + dx, j + dy)
        
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    res +=1
                    dfs(x, y)
        return res
                
                
            
            
            
            
                
