from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        target = len(word)
        visited = [[False]*m for _ in range(n)]
        def dfs(y,x,i):
            if i==target:
                return True
            for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
                ny,nx = y+dy,x+dx
                if ny<0 or ny>=n or nx<0 or nx>=m or visited[ny][nx]:
                    continue
                if board[ny][nx]==word[i]:
                    visited[ny][nx]=True
                    if dfs(ny,nx,i+1):
                        return True
                    visited[ny][nx]=False
        
        for y in range(n):
            for x in range(m):
                if board[y][x]==word[0]:
                    visited[y][x]=True
                    if dfs(y,x,1):
                        return True
                visited[y][x]=False
        return False