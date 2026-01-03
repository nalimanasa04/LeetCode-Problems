class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1000000007
        aba = 6
        abc = 6
        for _ in range(2, n + 1):
            aba, abc = (aba * 3 + abc * 2) % mod, (aba * 2 + abc * 2) % mod
        return (aba + abc) % mod
