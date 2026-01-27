import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))
            
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
            
            for v, w in rev_adj[u]:
                if dist[u] + 2 * w < dist[v]:
                    dist[v] = dist[u] + 2 * w
                    heapq.heappush(pq, (dist[v], v))
                    
        return dist[n-1] if dist[n-1] != float('inf') else -1