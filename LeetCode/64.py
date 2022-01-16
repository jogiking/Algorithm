# Time: MN개의 간선을 heap에 넣고 빼므로 O(MNlogMN)
# Space: O(MN)
# M, N은 grid의 가로와 세로의 크기

import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        height = len(grid)
        width = len(grid[0])
        visited = [[False]*width for _ in range(height)]
        dx = [1,0]
        dy = [0,1]
        queue = []
        heapq.heappush(queue, (grid[0][0], [0,0]))
        visited[0][0] = grid[0][0]
        
        if width < 2:
            return grid[0][0]
        
        while queue:
            value, v = heapq.heappop(queue)
            
            for i in range(2):
                ny, nx = dy[i]+v[0], dx[i]+v[1]
                if nx >= width or nx < 0 or ny >= height or ny < 0:
                    continue
                if visited[ny][nx]:
                    continue
                    
                cost = value+grid[ny][nx]                
                if ny == height-1 and nx == width-1:
                    return cost          
                
                visited[ny][nx] = True
                heapq.heappush(queue, (cost, [ny,nx]))