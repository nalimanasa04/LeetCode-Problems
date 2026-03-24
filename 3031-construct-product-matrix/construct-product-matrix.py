class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        arr = []
        for row in grid:
            arr.extend(row)
        k = len(arr)
        
        prefix = [1] * k
        suffix = [1] * k
        
        for i in range(1, k):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        for i in range(k-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        res = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append((prefix[idx] * suffix[idx]) % MOD)
                idx += 1
            res.append(row)
        
        return res