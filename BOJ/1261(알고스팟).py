import sys
import heapq
input = sys.stdin.readline

m,n = list(map(int,input().split()))
board = [list(map(int,input().rstrip())) for _ in range(n)]

def dijkstra():
    q = []
    heapq.heappush(q, (0,0,0))

    INF = 1e9
    distance = [[INF]*m for _ in range(n)]
    distance[0][0] = 0
    
    while q:
        d,y,x = heapq.heappop(q)
        for dy,dx in (0,1),(0,-1),(1,0),(-1,0):
            ny,nx = y+dy,x+dx
            if ny<0 or ny>=n or nx<0 or nx>=m:
                continue
            if (ny,nx) == (n-1,m-1):
                return d
            if d+board[ny][nx] < distance[ny][nx]:
                distance[ny][nx] = d+board[ny][nx]
                heapq.heappush(q, (distance[ny][nx],ny,nx))
    return board[0][0]
print(dijkstra())


#import sys
#import heapq
#input = sys.stdin.readline
#
#m,n = list(map(int,input().split()))
#board = [list(map(int,input().rstrip())) for _ in range(n)]
#
#def dijkstra():
#    heap = []
#    heapq.heappush(heap, (0,0,0))
#    visited = [[False]*m for _ in range(n)]
#    visited[0][0] = True
#    while heap:
#        v,y,x = heapq.heappop(heap)
#        for dy,dx in (0,1),(0,-1),(1,0),(-1,0):
#            ny,nx = y+dy,x+dx
#            if ny<0 or ny>=n or nx<0 or nx>=m or visited[ny][nx]:
#                continue
#            if (ny,nx) == (n-1,m-1):
#                return v
#            visited[ny][nx] = True
#            if board[ny][nx] == 0:
#                heapq.heappush(heap, (v,ny,nx))
#            else:
#                heapq.heappush(heap, (v+1,ny,nx))
#    return board[0][0]
#print(dijkstra())
