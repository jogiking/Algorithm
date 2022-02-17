m,n = list(map(int,input().split()))
board = [list(map(str,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def dfs(y,x,path):
    global visited
    visited[y][x] = True
    path += 1
    for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
        ny,nx = y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
            if board[ny][nx] == board[y][x]:
                path = dfs(ny,nx,path)
                
    return path

answer = [0,0]
for y in range(n):
    for x in range(m):
        if visited[y][x]:
            continue
        res = dfs(y,x,0)
        if board[y][x] == "W":
            answer[0]+=res**2
        else:
            answer[1]+=res**2

print(answer[0], answer[1])