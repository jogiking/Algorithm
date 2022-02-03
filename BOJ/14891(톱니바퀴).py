from collections import deque

board = [deque(map(int,list(input()))) for _ in range(4)]
n = int(input())
ops = [list(map(int, input().split())) for _ in range(n)]
need_to_rotate = []

def rotate(i, isClockwise):
    global board
    if isClockwise == -1:
        board[i].append(board[i].popleft())
    else:
        board[i].appendleft(board[i].pop())

# 시계방향(1)이 왼쪽, 반시계(-1)가 오른쪽
def move(phase, i, isClockwise):
    global board
    global need_to_rotate
    
    if phase == -1 and i<0:
        return
    if phase == 1 and i>3:
        return
    
    if phase == -1:
        if board[i][2] != board[i+1][6]:
            need_to_rotate.append((i, isClockwise))
            move(phase, i-1, -isClockwise)
    elif phase == 1:
        if board[i][6] != board[i-1][2]:
            need_to_rotate.append((i, isClockwise))
            move(phase, i+1, -isClockwise)

for i, isClockwise in ops:
    i-=1
    need_to_rotate = [(i, isClockwise)]
    move(-1, i-1, -isClockwise)
    move(1, i+1, -isClockwise)

    for i, isClockwise in need_to_rotate:
        rotate(i, isClockwise)

answer = 0
temp = 1
for i in range(len(board)):
    answer += board[i][0] * 2**i
print(answer)