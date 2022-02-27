import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

n,m,k = list(map(int,input().split()))
cost = list(map(int,input().split()))
graph = [[] for _ in range(n)]
visited = [False]*n
for _ in range(m):
    v, u = list(map(int,input().split()))
    graph[v-1].append(u-1)
    graph[u-1].append(v-1)

def dfs(v, c):
    c = min(cost[v], c)
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            c = dfs(u,c)
    return c
        
answer = 0
for i in range(n):
    if not visited[i]:
        answer += dfs(i, 987654321)
        
print(answer if k >= answer else "Oh no")
