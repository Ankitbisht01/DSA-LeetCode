'''
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
'''
#Solution
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, roots = len(grid), [*range(len(grid)**2*2)]
        
        def connect(i, j):
            roots[find(i)] = find(j)
        def find(i):
            if roots[i] != i: roots[i] = find(roots[i])
            return roots[i]
        def hash(x, y, direc):
            return (x*n + y)*2 + (direc < 2 if grid[x][y] == '\\' else 0 < direc < 3)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == ' ': connect(hash(i, j, 0), hash(i, j, 2)) 
                j < n-1 and connect(hash(i, j, 1), hash(i, j+1, 3))
                i < n-1 and connect(hash(i, j, 2), hash(i+1, j, 0))
        return len(set(find(i) for i in roots))