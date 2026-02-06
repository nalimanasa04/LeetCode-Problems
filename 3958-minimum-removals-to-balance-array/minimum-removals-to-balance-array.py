class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        ans = 0
        l = 0
        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            ans = max(ans, r - l + 1)
        return n - ans
