class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        neg = 0
        mn = float('inf')
        for row in matrix:
            for x in row:
                total += abs(x)
                if x < 0:
                    neg += 1
                if abs(x) < mn:
                    mn = abs(x)
        if neg % 2 == 0:
            return total
        return total - 2 * mn
