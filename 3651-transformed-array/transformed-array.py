class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n
        for i, v in enumerate(nums):
            if v == 0:
                result[i] = 0
            else:
                j = (i + v) % n
                result[i] = nums[j]
        return result
