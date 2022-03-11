from collections import deque

def bfs(board,y,x):
    q = deque([(y,x,0)])
    visited = [[False]*5 for _ in range(5)]
    visited[y][x] = True
    while q:
        y,x,v = q.popleft()
        for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if ny<0 or ny>=5 or nx<0 or nx>=5 or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if board[ny][nx]=="X":
                continue
            if board[ny][nx]=="P":
                return 0
            if v==0:
                q.append((ny,nx,v+1))
    return 1                
    
def get_answer(board):
    size=5
    persons=[]
    for y in range(size):
        for x in range(size):
            if board[y][x]=="P":
                persons.append((y,x))
    for y,x in persons:
        if bfs(board,y,x) == 0:
            return 0
    return 1
    
def solution(places):
    answer = []
    for place in places:
        board = [list(row) for row in place]
        answer.append(get_answer(board))
    return answer