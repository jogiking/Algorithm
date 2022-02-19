import sys
sys.setrecursionlimit(100000)

n,m,k = list(map(int,input().split()))
board = [["."]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for _ in range(k):
    r,c = list(map(int,input().split()))
    board[r-1][c-1] = "#"

def dfs(y,x,path):
    global visited
    visited[y][x] = True
    path+=1
    for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
        ny,nx=y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
            if board[ny][nx] == "#":
                path = dfs(ny,nx,path)
    return path

answer = 0
for y in range(n):
    for x in range(m):
        if board[y][x] == "#" and not visited[y][x]:
            res = dfs(y,x,0)
            answer = max(res, answer)
print(answer)
