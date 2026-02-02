from bisect import bisect_left, insort

class Solution:
    def minimumCost(self, nums, k, dist):
        arr = nums[1:]
        m = dist + 1
        need = k - 1

        window = sorted(arr[:m])
        cur = sum(window[:need])
        ans = cur

        for i in range(m, len(arr)):
            out = arr[i - m]
            idx = bisect_left(window, out)
            if idx < need:
                cur -= out
                if need < len(window):
                    cur += window[need]
            window.pop(idx)

            new = arr[i]
            idx = bisect_left(window, new)
            if idx < need:
                cur += new
                if need - 1 < len(window):
                    cur -= window[need - 1]
            insort(window, new)

            ans = min(ans, cur)

        return ans + nums[0]
