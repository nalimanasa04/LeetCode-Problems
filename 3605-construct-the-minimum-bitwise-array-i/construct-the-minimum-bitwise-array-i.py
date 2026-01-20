class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for p in nums:
            best = -1
            for k in range(p.bit_length()):
                if (p >> k) & 1:
                    ok = True
                    for j in range(k):
                        if ((p >> j) & 1) == 0:
                            ok = False
                            break
                    if ok:
                        best = p - (1 << k)
            ans.append(best)
        return ans
