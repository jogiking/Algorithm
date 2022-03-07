def find(key,board,m,n,y,x,target):
    count = 0
    for i in range(m):
        for j in range(m):
            if m<=y+i<n+m and m<=x+j<n+m:
                if key[i][j]==1:
                    if board[y+i][x+j]==1:
                        return False
                    else:
                        count+=1
    if count==target:
        return True
    else:
        return False
    
def solution(key, lock):
    m,n = len(key), len(lock)
    board = [[0]*(m+n+m) for _ in range(m+n+m)]
    empty = set()
    for y in range(n):
        for x in range(n):
            if lock[y][x]==0:
                empty.add((y+m,x+m))
    target = len(empty)
                
    if target==0:
        return True
    for y in range(n):
        for x in range(n):
            if lock[y][x]==1:
                board[m+y][m+x]=1
    for _ in range(4):
        for y in range(1,m+n):
            for x in range(1,m+n):
                if find(key,board,m,n,y,x,target):
                    return True
        key = list(map(list,zip(*key[::-1])))
                            
    return False