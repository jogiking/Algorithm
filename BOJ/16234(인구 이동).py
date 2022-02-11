from collections import deque

n,l,r = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def bfs(y,x):
    global visited
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    res = []
    while q:
        y,x = q.popleft()
        for dy,dx in (0,1),(0,-1),(-1,0),(1,0):
            ny,nx = dy+y, dx+x
            if ny<0 or ny>=n or nx<0 or nx>=n or visited[ny][nx]:
                continue
            if l<=abs(board[y][x]-board[ny][nx])<=r:
                q.append((ny,nx))
                visited[ny][nx] = True
                res.append((ny,nx))
    return res

def open_border(unions):
    for union in unions:
        value = sum(map(lambda t: board[t[0]][t[1]], union))//len(union)
        for y,x in union:
            board[y][x] = value

day = 0
while True:
    res = []
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                neighbor = bfs(y,x)
                if neighbor:
                    neighbor.append((y,x))
                    res.append(neighbor)
    if not res:
        break
    open_border(res)
    day+=1
    visited = [[False]*n for _ in range(n)]
print(day)
