class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)
        groups = {}
        ch = ord('a')
        res = [''] * n
        for i in range(n):
            p = find(i)
            if p not in groups:
                if ch > ord('z'):
                    return ""
                groups[p] = chr(ch)
                ch += 1
            res[i] = groups[p]
        word = "".join(res)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    val = 1
                    if i + 1 < n and j + 1 < n:
                        val += lcp[i + 1][j + 1]
                else:
                    val = 0
                if val != lcp[i][j]:
                    return ""
        return word