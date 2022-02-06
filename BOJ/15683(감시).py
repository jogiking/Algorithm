import copy

n, m = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(n)]
cameras = []
ans = 987654321

directions = [\
[[0],[1],[2],[3]],\
[[0,1],[2,3]],\
[[0,2],[0,3],[1,2],[1,3]],\
[[0,1,2],[0,1,3],[2,3,0],[2,3,1]],\
[[0,1,2,3]]]

def paint(board, y, x, directions):
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    for dir in directions:
        ny, nx = y, x
        while True:
            ny+=dy[dir]
            nx+=dx[dir]
            if 0<=ny<n and 0<=nx<m and board[ny][nx] != 6:
                board[ny][nx] = -1
            else:
                break

def count_blind_area(board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count+=1
    return count

def dfs(board, phase):
    global ans
    if phase == len(cameras):
        ans = min(ans, count_blind_area(board))
        return
    y, x, cam = cameras[phase]
    for direction in directions[cam-1]:
        temp = copy.deepcopy(board)
        paint(temp, y, x, direction)
        dfs(temp, phase+1)

for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5:
            cameras.append((i,j,board[i][j]))

dfs(board, 0)
print(ans)