import math

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        dist = [[math.inf] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        for u, v, w in zip(original, changed, cost):
            u_idx = ord(u) - ord('a')
            v_idx = ord(v) - ord('a')
            dist[u_idx][v_idx] = min(dist[u_idx][v_idx], w)
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            c = dist[s_idx][t_idx]
            
            if c == math.inf:
                return -1
            total_cost += c
            
        return total_cost