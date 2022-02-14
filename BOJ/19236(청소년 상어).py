import copy

board = [[] for _ in range(4)]
directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
fish = set(range(16))
for y in range(4):
    temp = list(map(lambda x:x-1, map(int,input().split())))
    for i in range(len(temp)//2):
        board[y].append(tuple(temp[2*i:2*i+2]))

def get_candidates(board,y,x,d):
    candidates = []
    dy,dx = directions[d]
    ny,nx = y,x
    while True:
        ny,nx = ny+dy, nx+dx
        if 0<=ny<4 and 0<=nx<4:
            if board[ny][nx] != (-1,0):
                candidates.append((ny,nx))
        else:
            break
    return candidates
    
def move(board,n,shark):
    for y in range(4):
        for x in range(4):
            _n,d = board[y][x]
            if _n == n:
                for i in range(8):
                    _d = (d+i)%8
                    dy,dx = directions[_d]
                    ny,nx = y+dy,x+dx
                    if 0<=ny<4 and 0<=nx<4 and shark!=[ny,nx]:
                        temp = board[ny][nx]
                        board[ny][nx] = (_n, _d)
                        board[y][x] = temp
                        return

def move_all(board,shark):
    for n in sorted(fish):
        move(board, n, shark)

def bfs(board,y,x,cost,d):
    global answer
    # 모든 물고기 이동
    move_all(board, [y,x])
    # 상어 이동
    candidates = get_candidates(board,y,x,d)
    if not candidates:
        answer = max(answer, cost)
        return
    for ny,nx in candidates:
        # 상어가 물고기 먹는 로직
        temp = copy.deepcopy(board)
        n,_d = temp[ny][nx]
        fish.remove(n)
        temp[ny][nx] = (-1,0)
        # 다음 사이클 시작
        bfs(temp,ny,nx,cost+n+1,_d)        
        fish.add(n)

answer = 0

# 0,0 위치 물고기 상어먹이기
n,d = board[0][0]
fish.remove(n)
board[0][0] = (-1,0)
# 탐색 시작
bfs(board,0,0,n+1,d)
print(answer)