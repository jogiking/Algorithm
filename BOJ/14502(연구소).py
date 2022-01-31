from collections import deque
import copy

n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

def count_safearea(board):
    row, col = len(board), len(board[0])
    count = 0
    for y in range(row):
        for x in range(col):
            if board[y][x] == 0:
                count+=1
    return count

def bfs(i, j, board):
    row, col = len(board), len(board[0])
    q = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    if board[i][j] == 2:
        q.append((i,j))
    while q:
        y,x = q.popleft()
        for step in range(len(dy)):
            ny,nx = y+dy[step], x+dx[step]
            if ny<0 or ny>=row or nx<0 or nx>=col:
                continue
            if board[ny][nx] == 0 and board[y][x] == 2:
                board[ny][nx] = 2
                q.append((ny,nx))

def is_empty_spaces(board, positions):
    for element in positions:
        y, x = convert(len(board[0]), element)
        if board[y][x] != 0:
            return False
    return True

def convert(col, index):
    return index//col, index%col

def get_positions(board):
    res = []
    for i in range(row*col):
        for j in range(i+1, row*col):
            for k in range(j+1, row*col):     
                if is_empty_spaces(board, [i,j,k]):
                    temp = []
                    for element in [i,j,k]:
                        temp.append(convert(col, element))
                    res.append(temp)
    return res

row, col = len(board), len(board[0])

max_value = -1
for positions in get_positions(board):
    t_board = copy.deepcopy(board)
    for y,x in positions:
        t_board[y][x] = 1

    for i in range(row):
        for j in range(col):
            if t_board[i][j] == 2:
                bfs(i,j, t_board)
                
    max_value = max(count_safearea(t_board), max_value)            
            
print(max_value)