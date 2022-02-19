import sys
from collections import deque

n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

def bfs(y,x,option):
    q = deque([(y,x,board[y][x])])
    visited[y][x] = True
    while q:
        y,x,v = q.popleft()
        for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if option:
                    if v == "B" and board[ny][nx] != "B":
                        continue
                    if v != "B" and board[ny][nx] == "B":
                        continue
                    visited[ny][nx] = True
                    q.append((ny,nx,v))
                else:
                    if board[ny][nx] == v:
                        visited[ny][nx] = True
                        q.append((ny,nx,v))

res1 = 0
visited = [[False]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            res1+=1
            bfs(y,x,False)

res2 = 0
visited = [[False]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            res2+=1
            bfs(y,x,True)

print(res1, res2)
