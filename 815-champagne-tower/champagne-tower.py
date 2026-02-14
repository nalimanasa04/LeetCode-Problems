class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 2)
        dp[0] = float(poured)
        for r in range(query_row):
            next_dp = [0.0] * (query_row + 2)
            for c in range(r + 1):
                overflow = max(0.0, dp[c] - 1.0) / 2.0
                if overflow > 0:
                    next_dp[c] += overflow
                    next_dp[c + 1] += overflow
            dp = next_dp
        return min(1.0, dp[query_glass])
