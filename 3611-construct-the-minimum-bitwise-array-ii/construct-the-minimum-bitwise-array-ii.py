class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for p in nums:
            if p & 1 == 0:
                ans.append(-1)
                continue
            s = 0
            while p & (1 << s):
                s += 1
            ans.append(p - (1 << (s - 1)))
        return ans
