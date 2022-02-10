# 시간초과가 떠서 pypy로 제출함

r,c,t = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(r)]
machine = []
dusts = []
# 청정기, 먼지 위치 찾기
for y in range(r):
    for x in range(c):
        if board[y][x] == -1:
            machine.append((y,x))
        elif board[y][x] > 0:
            dusts.append((y,x,board[y][x]))

def find_dust():
    global dusts
    temp = []
    for y in range(r):
        for x in range(c):
            if board[y][x] > 0:
                temp.append((y,x,board[y][x]))
    dusts = temp

def spread():
    global dusts

    for y,x,v in dusts:
        count = 0
        for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
            ny,nx = y+dy, x+dx
            if ny<0 or ny>=r or nx<0 or nx>=c:
                continue
            if (ny,nx) in machine:
                continue
            board[ny][nx]+=v//5
            count+=1
        board[y][x]-=(v//5)*count
        

def machine_run():
    top, bottom = machine
    for y in range(top[0]-1,0,-1):
        board[y][0] = board[y-1][0]
    for x in range(c-1):
        board[0][x] = board[0][x+1]
    for y in range(top[0]):
        board[y][c-1] = board[y+1][c-1]
    for x in range(c-1,1,-1):
        board[top[0]][x] = board[top[0]][x-1]
    board[top[0]][1] = 0

    for y in range(bottom[0]+1,r-1):
        board[y][0] = board[y+1][0]
    for x in range(c-1):
        board[r-1][x] = board[r-1][x+1]
    for y in range(r-1,bottom[0],-1):
        board[y][c-1] = board[y-1][c-1]
    for x in range(c-1,1,-1):
        board[bottom[0]][x] = board[bottom[0]][x-1]
    board[bottom[0]][1] = 0

for _ in range(t):
    spread()
    machine_run()
    find_dust()

answer = 0
for dust in dusts:
    answer+=dust[2]
print(answer)
