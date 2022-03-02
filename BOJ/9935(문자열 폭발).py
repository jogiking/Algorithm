import sys
input = sys.stdin.readline

s = list(input().strip())
c = input().strip()
stack = []

def check():
    global stack
    if len(stack)<len(c):
        return False
    for j in range(len(c)):
        if c[-1-j] != stack[-1-j]:
            return False

    for _ in range(len(c)):
        if not stack:
            break
        stack.pop()
    return True

for i in range(len(s)):
    stack.append(s[i])
    if i-len(c)+1>=0:
        while True:
            if not check():
                break
if stack:
    print("".join(stack))
else:
    print("FRULA")