# 시간제한이 굉장히 깐깐한 문제.
# 시간초과가 떠서 pypy로 제출하니 메모리 초과가 나서 해결하는데 오래걸렸다.
# 메모리 초과 문제는 bfs에서 중복된 부분을 제거하는 방법으로 해결함.(set을 사용하여 나중에 변환)
# 풀이핵심 아이디어는 백조가 있는지 확인하는 bfs를 반복해서 돌릴 때, 이때 다음 bfs에 사용할 큐를 미리 준비하는 것이다.
# bfs를 순회하면 물과 얼음판 경계를 모두 알게 되는데(y,x와 ny,nx),
# ny,nx를 새로운 큐에 저장하고 다음번째 확인할 때 이 큐를 사용한다.
# 그런데 이 방법으로는 파이썬은 시간초과가 나는것 같다...
# 다른 풀이 방법을 찾아보니 "BFS+Binary Search", "BFS+서로소 집합(Disjoint Set / Union find)"로 해결 할 수 있다고 한다.

from collections import deque

r,c = list(map(int,input().split()))
board = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
birds = deque()
water = deque()
bird_position = []

def find():
    global bird_position
    global water
    # 모든 물과 새의 위치를 찾는다
    for y in range(r):
        for x in range(c):
            if board[y][x] == ".":
                water.append((y,x))
            elif board[y][x] == "L":
                bird_position.append((y,x))
                water.append((y,x)) # 새도 물로 처리

# 새확산 -> 다음 새확산 리스트를 만듬
# 물확산(녹음) -> 다음 물 녹음 리스트를 만듬
def solution(birds, water, bird_position):
    answer = 0
    y,x = bird_position[0]
    visited[y][x] = True
    while True:
        next_birds = deque()
        next_water = deque()
        temp = set()
        while water:
            y,x = water.popleft()
            board[y][x] = "."
            for dy,dx in (1,0),(-1,0),(0,-1),(0,1):
                ny,nx = y+dy,x+dx
                if ny<0 or ny>=r or nx<0 or nx>=c:
                    continue
                if board[ny][nx] == "X":
                    temp.add((ny,nx))
                    # next_water.append((ny,nx)) # 메모리 초과 해결한 부분
        # water = next_water
        water = deque(temp) # 메모리 초과 해결한 부분

        temp = set()
        while birds:
            y,x = birds.popleft()
            for dy,dx in (1,0),(-1,0),(0,-1),(0,1):
                ny,nx = y+dy,x+dx
                if ny<0 or ny>=r or nx<0 or nx>=c:
                    continue
                if visited[ny][nx]:
                    continue
                if (ny,nx) == bird_position[1]:
                    return answer
                if board[ny][nx] == "X":
                    # next_birds.append((ny,nx))
                    temp.add((ny,nx)) # 메모리 초과 해결한 부분
                else:
                    visited[ny][nx] = True
                    birds.append((ny,nx))
        birds = deque(temp) #next_birds # 메모리 초과 해결한 부분
        answer += 1
find()
birds.append(bird_position[0])
print(solution(birds, water, bird_position))
