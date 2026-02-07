class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = 0
        
        for c in s:
            if c == 'b':
                b_count += 1
            else:
                deletions = min(deletions + 1, b_count)
        
        return deletions
