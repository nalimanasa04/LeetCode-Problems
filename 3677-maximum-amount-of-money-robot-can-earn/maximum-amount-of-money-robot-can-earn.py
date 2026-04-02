class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        dp = [[[-10**15]*3 for _ in range(n)] for _ in range(m)]
        
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                if k > 0:
                    dp[0][0][k] = 0
                else:
                    dp[0][0][k] = coins[0][0]
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue
                    val = coins[i][j]
                    best = -10**15
                    
                    if i > 0:
                        if val >= 0:
                            best = max(best, dp[i-1][j][k] + val)
                        else:
                            best = max(best, dp[i-1][j][k] + val)
                            if k > 0:
                                best = max(best, dp[i-1][j][k-1])
                    
                    if j > 0:
                        if val >= 0:
                            best = max(best, dp[i][j-1][k] + val)
                        else:
                            best = max(best, dp[i][j-1][k] + val)
                            if k > 0:
                                best = max(best, dp[i][j-1][k-1])
                    
                    dp[i][j][k] = best
        
        return max(dp[m-1][n-1])