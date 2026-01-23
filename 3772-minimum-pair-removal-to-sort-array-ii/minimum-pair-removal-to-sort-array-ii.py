import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        val = nums[:]
        prev = list(range(-1, n - 1))
        nxt = list(range(1, n + 1))
        alive = [True] * n

        bad = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                bad += 1

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (val[i] + val[i + 1], i))

        def valid(i):
            return i != -1 and alive[i] and nxt[i] != n and alive[nxt[i]]

        ops = 0

        while bad > 0:
            while heap:
                s, i = heapq.heappop(heap)
                if valid(i) and val[i] + val[nxt[i]] == s:
                    break
            j = nxt[i]
            pi = prev[i]
            nj = nxt[j]

            if pi != -1 and alive[pi] and val[pi] > val[i]:
                bad -= 1
            if val[i] > val[j]:
                bad -= 1
            if nj != n and alive[nj] and val[j] > val[nj]:
                bad -= 1

            val[i] += val[j]
            alive[j] = False
            nxt[i] = nj
            if nj != n:
                prev[nj] = i

            if pi != -1 and alive[pi] and val[pi] > val[i]:
                bad += 1
            if nj != n and alive[nj] and val[i] > val[nj]:
                bad += 1

            if pi != -1 and alive[pi]:
                heapq.heappush(heap, (val[pi] + val[i], pi))
            if nj != n and alive[nj]:
                heapq.heappush(heap, (val[i] + val[nj], i))

            ops += 1

        return ops
