from itertools import combinations

n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

stores = []
homes = []
answer = 987654321
def distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

# step1) 각 치킨집의 위치정보stores(y,x)배열과 고객집 위치정보 homes(y,x)배열을 만든다
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            homes.append((y,x))
        elif board[y][x] == 2:
            stores.append((y,x))
# step2) 치킨배열에서 m개를 뽑은 배열picks을 만든다
for picks in list(combinations(stores, m)):
    # step3) picks를 순회하면서 도시의 치킨거리를 계산한다
    # step4) 도시의 치킨거리를 구하는 방법:
    # 각 집마다 가장 가까운 치킨집들의 최소 거리를 구하고 더한다. 이값이 최소가 나와야함
    chicken_dist = []
    for home in homes:
        dist = 987654321
        for p in picks:
            dist = min(distance(home, p), dist)
        chicken_dist.append(dist)
    answer = min(answer, sum(chicken_dist))

print(answer)