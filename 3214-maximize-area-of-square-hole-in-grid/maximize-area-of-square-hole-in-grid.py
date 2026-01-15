class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def longest_consecutive(arr):
            if not arr:
                return 1
            arr.sort()
            best = cur = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                else:
                    best = max(best, cur)
                    cur = 1
            return max(best, cur) + 1

        h = longest_consecutive(hBars)
        v = longest_consecutive(vBars)
        side = min(h, v)
        return side * side
