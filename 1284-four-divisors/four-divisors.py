from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            d = []
            i = 1
            while i * i <= n:
                if n % i == 0:
                    d.append(i)
                    if i != n // i:
                        d.append(n // i)
                    if len(d) > 4:
                        break
                i += 1
            if len(d) == 4:
                total += sum(d)
        return total
