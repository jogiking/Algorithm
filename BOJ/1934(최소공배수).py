import sys
input = sys.stdin.readline

t = int(input())

def gcd(a,b):
    if b == 0:
        return a
    if a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)

for _ in range(t):
    a,b = list(map(int,input().split()))
    temp = gcd(a,b)
    print((a//temp)*b)
