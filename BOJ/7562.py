from collections import deque

def calculate_cost():
    size = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    board = [[0] * size for _ in range(size)]

    dy = [2,1,-1,-2,-2,-1,1,2]
    dx = [1,2,2,1,-1,-2,-2,-1]

    q = deque([start])
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0<= nx < size and 0<= ny < size:
                if board[ny][nx] == 0 and [ny, nx] != start:
                    q.append([ny,nx])
                    board[ny][nx] = board[y][x] + 1
    print(board[end[0]][end[1]])

numberOfTest = int(input())
for _ in range(numberOfTest):
    calculate_cost()
