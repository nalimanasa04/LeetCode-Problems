from heapq import nlargest

class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        s = set()
        
        for i in range(m):
            for j in range(n):
                s.add(grid[i][j])
                k = 1
                while i-k >= 0 and i+k < m and j-k >= 0 and j+k < n:
                    total = 0
                    x, y = i-k, j
                    for t in range(k):
                        total += grid[x+t][y+t]
                    x, y = i, j+k
                    for t in range(k):
                        total += grid[x+t][y-t]
                    x, y = i+k, j
                    for t in range(k):
                        total += grid[x-t][y-t]
                    x, y = i, j-k
                    for t in range(k):
                        total += grid[x-t][y+t]
                    s.add(total)
                    k += 1
        
        return nlargest(3, s)