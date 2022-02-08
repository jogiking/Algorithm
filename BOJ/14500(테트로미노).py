# 세번째 방법
# 두번째 방법에서 ㅗ 블록처리 방법을 변경한 방법
# ㅗ블록은 깊이가 2인 경우일 때 현재 위치에서 다시한번 탐색을 해주면 되었음
n, m = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(n)]
max_value = max(map(max, board))
visited = [[False]*m for _ in range(n)]

answer = 0
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def dfs(y, x, phase, cost):
    global answer
    if cost + (4-phase)*max_value <= answer:
        return
    if phase == 4:
        answer = max(answer, cost)
        return
    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        if ny<0 or ny>=n or nx<0 or nx>=m or visited[ny][nx]:
            continue
        if phase == 1:
            visited[ny][nx] = True
            dfs(y,x,phase+1,cost+board[ny][nx])
            visited[ny][nx] = False
        visited[ny][nx] = True
        dfs(ny,nx,phase+1,cost+board[y][x])
        visited[ny][nx] = False

for y in range(n):
    for x in range(m):
        visited[y][x] = True
        dfs(y,x,0,0)
        visited[y][x] = False

print(answer)

# 두번째 방법
# 깊이가 4인 dfs를 사용하여 품.
# ㅗ 블록의 경우는 따로 계산함.
# 빠른 종료를 위해 남은 탐색에서 모두 최대값이 나와도 현재 최대값을 넘을 수 있는지 확인하는 부분이 있어야 했음(없으면 시간초과)
# n, m = list(map(int,input().split()))
# board = [list(map(int,input().split())) for _ in range(n)]
# max_value = max(map(max, board))
# visited = [[False]*m for _ in range(n)]
# answer = 0
# dy = [0,0,1,-1]
# dx = [1,-1,0,0]
# def dfs(y, x, phase, cost):
#     global answer
#     if cost + (4-phase)*max_value <= answer:
#         return
#     if phase == 4:
#         answer = max(answer, cost)
#         return
#     for i in range(4):
#         ny,nx = y+dy[i], x+dx[i]
#         if ny<0 or ny>=n or nx<0 or nx>=m or visited[ny][nx]:
#             continue
#         visited[ny][nx] = True
#         dfs(ny,nx,phase+1,cost+board[y][x])
#         visited[ny][nx] = False
# for y in range(n):
#     for x in range(m):
#         visited[y][x] = True
#         dfs(y,x,0,0)
#         visited[y][x] = False
# blocks = [[[1,0],[1,1],[1,0]],[[1,1,1],[0,1,0]],[[0,1,0],[1,1,1]],[[0,1],[1,1],[0,1]]]
# for block in blocks:
#     for y in range(n-len(block)+1):
#         for x in range(m-len(block[0])+1):
#             cost = 0
#             for u in range(len(block)):
#                 for v in range(len(block[0])):
#                     if block[u][v] == 1:
#                         cost += board[y+u][x+v]
#             answer = max(answer, cost)
# print(answer)

# 첫번쨰 방법
# bf로 품. 시간초과가 떠서 pypy로 제출해야 통과되었음
# def rotate(block):
#     return list(map(list,zip(*block[::-1])))
# def flip(block):
#     return list(map(lambda x: x[::-1], block))
# def count_value(block):
#     res = 0
#     for y in range(n-len(block)+1):
#         for x in range(m-len(block[0])+1):
#             temp = 0
#             for u in range(len(block)):
#                 for v in range(len(block[0])):
#                     if block[u][v] == 1:
#                         temp += board[y+u][x+v]
#             res = max(res, temp)
#     return res
# blocks = [[[1,1,1,1]], [[1,1],[1,1]], [[1,0],[1,0],[1,1]], [[1,0],[1,1],[0,1]], [[1,1,1],[0,1,0]]]
# n, m = list(map(int,input().split()))
# board = [list(map(int,input().split())) for _ in range(n)]
# answer = -1
# for block in blocks:
#     rotate_block = block
#     for _ in range(4):
#         answer = max(answer, count_value(rotate_block))
#         flip_block = flip(rotate_block)
#         answer = max(answer, count_value(flip_block))
#         rotate_block = rotate(rotate_block)
# print(answer)
