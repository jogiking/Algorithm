from bisect import bisect_left
from sys import stdin
input = stdin.readline
n,h = list(map(int,input().split()))
top = []
bottom = []
for i in range(n):
    if i%2 == 0:
        bottom.append(int(input()))
    else:
        top.append(h-int(input()))

top.sort()
bottom.sort()

answer = [987654321, 0]
for i in range(1,h+1):
    temp = len(bottom)-bisect_left(bottom, i)
    temp += bisect_left(top, i)
    
    if temp == answer[0]:
        answer[1]+=1
    elif temp < answer[0]:
        answer = [temp, 1]

print(answer[0], answer[1])
