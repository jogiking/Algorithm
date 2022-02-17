n = int(input())
board = [list(map(int,input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def dfs(y,x,size):
    global visited
    visited[y][x] = True
    size += 1
    for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
        ny,nx = y+dy,x+dx
        if ny<0 or ny>=n or nx<0 or nx>=n or visited[ny][nx]:
            continue
        if board[ny][nx] == 1:
            size = dfs(ny,nx,size)
    return size

answer = []

for y in range(n):
    for x in range(n):
        if board[y][x]==1 and not visited[y][x]:
            answer.append(dfs(y,x,0))

print(len(answer))
for element in sorted(answer):
    print(element)
