class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        curr_area = 0

        def dfs(x, y):
            nonlocal curr_area
            dirs = [(0,-1), (1,0), (0,1), (-1,0)]
            for dx, dy in dirs:
                row, col = x + dx, y + dy
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                    continue
                
                grid[row][col] = 0
                curr_area += 1
                dfs(row, col)

        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    curr_area = 1
                    dfs(i, j)
                    max_area = max(max_area, curr_area)
        
        return max_area