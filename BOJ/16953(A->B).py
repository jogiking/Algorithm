from collections import deque
a,b = list(map(int,input().split()))

def bfs(start, target):
    q = deque([(start,1)])
    while q:
        n, count = q.popleft()
        if n == target:
            return count
        if n > target:
            continue
        q.append((2*n, count+1))
        q.append((10*n+1, count+1))
    return -1

print(bfs(a,b))
