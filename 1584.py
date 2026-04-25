import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        result = 0
        edges_used = 0
        
        while edges_used < n:
            cost, i = heapq.heappop(heap)
            
            if visited[i]:
                continue
            
            visited[i] = True
            result += cost
            edges_used += 1
            
            x1, y1 = points[i]
            
            for j in range(n):
                if not visited[j]:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, j))
        
        return result
