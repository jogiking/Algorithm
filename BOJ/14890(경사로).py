n, size = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

def check(row, size):
    n = len(row)
    visited = [False]*n
    i = 0
    while i < n-1: 
        diff = row[i+1]-row[i]
        if diff == 1:
            for j in range(size):
                k = i-j
                if k < 0 or visited[k]:
                    return False
                if row[i] != row[k]:
                    return False
                visited[k] = True
            i+=1
        elif diff == -1:
            for j in range(size):
                k = (i+1)+j
                if k >= n:
                    return False
                if i+1 > n or row[i+1] != row[k]:
                    return False
                visited[k] = True
            i+=size
        elif diff > 1 or diff < -1:
            return False
        elif diff == 0:
            i+=1
    return True

answer = 0
for row in list(map(list,zip(*board))):
    if check(row[:], size):
        answer+=1
for row in board:
    if check(row[:], size):
        answer+=1

print(answer)
