n,k = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(n)]
towers = {}
stacks = [[[] for _ in range(n)] for _ in range(n)]
directions = [(0,1),(0,-1),(-1,0),(0,1)]

for i in range(k):
    y,x,d = list(map(lambda x:x-1,map(int,input().split())))
    towers[i] = (y,x,d)
    stacks[y][x].append((i, d))
    
def op(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    elif d==3:
        return 2

def move(y,x,d,ny,nx,i):
    if ny<0 or ny>=n or nx<0 or nx>=n or board[ny][nx] == 2: # 밖을 나갈 때나 파란색
        dy,dx = directions[op(d)]
        ny,nx = y+dy, x+dx
        if ny<0 or ny>=n or nx<0 or nx>=n or board[ny][nx] == 2: # 반대쪽이 벗어나는 경우 = 파란색
            return y,x
        elif board[ny][nx] == 1: # 빨간색 = 순서 뒤집기
            for _ in range(len(stacks[y][x])-i):
                stacks[ny][nx].append(stacks[y][x].pop())
        elif board[ny][nx] == 0: # 흰색 = 순서대로
            stacks[ny][nx]+=stacks[y][x][i:]
            for _ in range(len(stacks[y][x])-i):
                stacks[y][x].pop()
    elif board[ny][nx] == 1: # 빨간색 = 순서 뒤집기
        for _ in range(len(stacks[y][x])-i):
            stacks[ny][nx].append(stacks[y][x].pop())
    elif board[ny][nx] == 0: # 흰색
        stacks[ny][nx]+=stacks[y][x][i:]
        for _ in range(len(stacks[y][x])-i):
            stacks[y][x].pop()
    return ny,nx

def solution():
    t = 0
    # 모든 말마다 반복
    while t<=1000:
        t+=1
        for i in range(k):
            y,x,d = towers[i]
            dy,dx = directions[d]
            ny,nx = y+dy, x+dx
            for j in range(len(stacks[y][x])):
                if stacks[y][x][j][0] == i:
                    temp = stacks[y][x][j:]
                    _ny,_nx = move(y,x,d,ny,nx,j)
                    if y==_ny and x==_nx:
                        towers[i] = (_ny,_nx,op(d))
                    else:
                        for _i,_d in temp:
                            towers[_i] = (_ny,_nx,_d)
                        if len(stacks[_ny][_nx])>=4:
                            return t
                    break
    return t

t = solution()
t = -1 if t>1000 else t
print(t)