n = int(input())
infos = [list(map(int,input().split())) for _ in range(n)]

dy = [1,0,-1,0]
dx = [0,-1,0,1]

def get_order(dir, gen):
    stack = [dir]
    for _ in range(gen):
        for i in reversed(range(len(stack))):
            stack.append((stack[i]+1)%4)
    return stack
points = set()
for y,x,d,g in infos:
    points.add((y,x))
    for i in get_order(d,g):
        y+=dy[i]
        x+=dx[i]
        points.add((y,x))

answer = 0
for p in points:
    if (p[0]+1, p[1]) not in points:
        continue
    if (p[0], p[1]+1) not in points:
        continue
    if (p[0]+1, p[1]+1) not in points:
        continue
    answer += 1
print(answer)