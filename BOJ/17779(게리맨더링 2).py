n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

def dfs(r,c,v,bd):
    if r<0 or r>=n or c<0 or c>=n or bd[r][c]!=0:
        return
    bd[r][c]=v
    for dy,dx in (0,1),(0,-1),(1,0),(-1,0):
        nr,nc = r+dy, c+dx
        dfs(nr,nc,v,bd)

def divide(x,y,d1,d2):
    bd = [[0]*n for _ in range(n)]

    # 5의 경계선 그리기
    for i in range(d1+1):
        bd[x+i][y-i] = 5
        bd[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        bd[x+i][y+i] = 5
        bd[x+d1+i][y-d1+i] = 5
    
    # 1,2,3,4 영역 수평수직 기둥 그리기
    for i in range(x):
        bd[i][y] = 1
    for i in range(y-d1):
        bd[x+d1][i] = 3
    for i in range(y+d2+1, n):
        bd[x+d2][i] = 2
    for i in range(x+d1+d2+1, n):
        bd[i][y-d1+d2] = 4

    # 나머지 1,2,3,4 영역 그리기
    dfs(0,0,1,bd)
    dfs(0,n-1,2,bd)
    dfs(n-1,0,3,bd)
    dfs(n-1,n-1,4,bd)
    return bd

answer = 987654321
for x in range(n):
    for y in range(n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if x+d1+d2>=n or y-d1<0 or y+d2>=n:
                    continue
                values = [0]*5
                bd = divide(x,y,d1,d2)
                for i in range(n):
                    for j in range(n):
                        if bd[i][j] == 0:
                            values[4]+=board[i][j]
                        else:
                            values[bd[i][j]-1]+=board[i][j]
                values.sort()
                diff = values[-1]-values[0]
                answer = min(answer, diff)
print(answer)