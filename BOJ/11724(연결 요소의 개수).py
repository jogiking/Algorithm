# 입력을 받을 때 input()을 사용하니 시간초과가 떴다.
# 이제부터는 sys.stdin.readline()을 사용해야겠다.

import sys
from collections import deque

n,m = list(map(int, sys.stdin.readline().split()))
board = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    y,x = list(map(int, sys.stdin.readline().split()))
    board[y].append(x)
    board[x].append(y)

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        i = q.popleft()
        for v in board[i]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        answer+=1
        bfs(i)

print(answer)
