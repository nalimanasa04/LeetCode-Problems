class Solution:
    def maxProduct(self, root):
        import sys
        sys.setrecursionlimit(10**7)
        MOD = 10**9 + 7

        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)
        best = 0

        def dfs(node):
            nonlocal best
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            best = max(best, s * (total - s))
            return s

        dfs(root)
        return best % MOD
