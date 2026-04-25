import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        
        heap = [(0, 0, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            effort, x, y = heapq.heappop(heap)
            
            if x == m - 1 and y == n - 1:
                return effort
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))
        
        return 0
