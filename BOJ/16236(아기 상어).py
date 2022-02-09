# 1. 상어가 지나갈 수 있는지 아닌지 조건을 빠짐없이 잘 읽어내야 했음
# 2. 상어 크기가 커질 수 있는 조건이 자기와 같은 크기의 먹이를 먹었을 때가 아니었음. 1번과 함께 조건을 잘못 이해해서 풀이시간이 오래걸림
# 3. 막혀있는 경우에 대한 처리도 했어야 함

from collections import deque

INF = 987654321
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
shark = []
shark_size = 2
fish = set()
for y in range(n):
    for x in range(n):
        if board[y][x] == 9:
            shark = [y,x]
        elif board[y][x] > 0:
            fish.add((y,x))

def bfs(y,x):
    bd = [[INF]*n for _ in range(n)]
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    q = deque()
    visited = [[False]*n for _ in range(n)]    
    q.append((y,x,0))
    visited[y][x] = True
    while q:
        y,x,value = q.popleft()
        bd[y][x] = value
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if ny<0 or ny>=n or nx<0 or nx>=n or visited[ny][nx]:
                continue
            if 0<=board[ny][nx]<=shark_size or board[ny][nx] == 9:
                visited[ny][nx] = True
                q.append((ny,nx,value+1))
    return bd

def get_candidates():
    candidates = []
    distance = bfs(shark[0],shark[1])
    for y,x in fish:
        if 0<board[y][x]<shark_size:
            dist = distance[y][x]
            if dist == INF:
                continue
            candidates.append((y,x,dist))
    candidates.sort(key=lambda x: (x[2], x[0], x[1]))
    return candidates

answer = 0
eat_count = 0
while True:
    candi = get_candidates()
    if not candi:
        break
    y,x,distance = candi[0]
    shark = [y,x]
    # 물고기 삭제
    fish.remove((y,x))
    answer+=distance
    # 아기상어 크기 갱신
    eat_count+=1
    if eat_count == shark_size:
        shark_size+=1
        eat_count=0
print(answer)
