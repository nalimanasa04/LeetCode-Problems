class Solution:
    def minimumPairRemoval(self, nums):
        def is_non_decreasing(a):
            return all(a[i] >= a[i - 1] for i in range(1, len(a)))

        ops = 0
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1
        return ops
