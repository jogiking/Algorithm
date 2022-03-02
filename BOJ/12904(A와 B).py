import sys
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

def solution(s,t):
    while s!=t:
        if len(t)==0:
            return 0
        if t[-1] == "A":
            t = t[:-1]
        else:
            t = t[::-1]
            t = t[1:]
    return 1

print(solution(s,t))
        
