from collections import deque
col, row = list(map(int, input().split()))
board = []
q = deque()
for y in range(row):
  board.append(list(map(int, input().split())))
  for x in range(col):
    if board[-1][x] == 1:
      q.append((y,x,0))

days = [[0]*col for _ in range(row)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def find_answer(board, days):
  ans = 0
  for y in range(row):
    for x in range(col):
      if board[y][x] == 0:
        return -1
      ans = max(days[y][x], ans)
  return ans

def bfs(q, board, days):
  while q:
    y, x, day = q.popleft()
    for i in range(len(dy)):
      ny, nx = y+dy[i], x+dx[i]
      if 0<=ny<row and 0<=nx<col and board[ny][nx] == 0:
        q.append((ny,nx,day+1))
        days[ny][nx] = day+1
        board[ny][nx] = day+1

bfs(q, board, days)
print(find_answer(board, days))