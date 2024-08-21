'''
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.
'''
#Solution
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands(g):
            def dfs(i, j):
                if i < 0 or i >= len(g) or j < 0 or j >= len(g[0]) or g[i][j] == 0:
                    return
                g[i][j] = 0
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    dfs(x, y)
            
            island_count = 0
            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j] == 1:
                        dfs(i, j)
                        island_count += 1
            return island_count
        
        def is_disconnected():
            return count_islands([row[:] for row in grid]) != 1
        
        if is_disconnected():
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected():
                        return 1
                    grid[i][j] = 1
        
        return 2