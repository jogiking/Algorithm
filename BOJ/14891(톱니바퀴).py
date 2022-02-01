from collections import deque

board = [deque(map(int,list(input()))) for _ in range(4)]
n = int(input())
ops = [list(map(int, input().split())) for _ in range(n)]
def rotate(i, isClockwise):
    global board
    if isClockwise == 1:
        board[i].append(board[i].popleft())
    else:
        board[i].appendleft(board[i].pop())

# 시계방향(1)이 왼쪽, 반시계(-1)가 오른쪽
def move(phase, i, isClockwise):
    global board
    
    if phase == -1 and i<1:
        return
    if phase == 1 and i>4:
        return
    i-=1
    if phase == -1:
        if board[i][2] != board[i+1][2]:
            rotate(i, isClockwise)
            move(phase, i-1, -isClockwise)
    elif phase == 1:
        if board[i][2] != board[i-1][2]:
            rotate(i, isClockwise)
            move(phase, i+1, -isClockwise)

for i, isClockwise in ops:
    rotate(i-1, isClockwise)
    move(-1, i-1, 1)
    move(1, i+1, -1)

for row in board:
    print(row)
