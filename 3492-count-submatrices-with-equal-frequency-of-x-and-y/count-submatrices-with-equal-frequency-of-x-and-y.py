class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        ps = [[0]*n for _ in range(m)]
        px = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                ps[i][j] = val
                px[i][j] = 1 if grid[i][j] == 'X' else 0
                
                if i > 0:
                    ps[i][j] += ps[i-1][j]
                    px[i][j] += px[i-1][j]
                if j > 0:
                    ps[i][j] += ps[i][j-1]
                    px[i][j] += px[i][j-1]
                if i > 0 and j > 0:
                    ps[i][j] -= ps[i-1][j-1]
                    px[i][j] -= px[i-1][j-1]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if ps[i][j] == 0 and px[i][j] > 0:
                    ans += 1
        
        return ans