n, m = list(map(int, input().split()))
pos = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def clean(visited, y, x, dir):
    global n, m, answer
    visited[y][x] = -1 # 현재 위치를 청소
    answer += 1
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    next_dir = dir
    count = 0
    while True:
        next_dir = (next_dir-1)%4
        ny, nx = y+dy[next_dir], x+dx[next_dir]
        count += 1
        
        if next_dir == dir and count>4:
            y, x = y+dy[dir-2], x+dx[dir-2]
            next_dir = dir
            if y<0 or y>=n or x<0 or x>=m or visited[y][x] == 1: # 후진할 수 없는경우(d)
                break              
        if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0: # a
            visited[ny][nx] = -1 # 현재위치를 청소
            answer += 1
            y, x, dir = ny, nx, next_dir # 1번작업으로 이동
        
clean(board, pos[0], pos[1], pos[2])
print(answer)