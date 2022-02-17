# 정말 오래걸린 문제
# 33%에서 틀렸습니다 뜸
# 출력할 때 [1, 2, 3, 4] 가 아닌 [1,2,3,4]로 출력해야한다는 것을 늦게 알게됨

from collections import deque

t = int(input())

for _ in range(t):
    temp = list(map(str,input()))
    funcs = [temp[0]]
    for i in range(1,len(temp)):
        if temp[i] == "R" and funcs and temp[i]==funcs[-1]:
            funcs.pop()
        else:
            funcs.append(temp[i])

    size = int(input())
    arr = deque(input()[1:-1].split(","))
    if size == 0:
        arr = deque()
    
    flag = False
    isReverse = False
    for func in funcs:
        if func == "R":
            isReverse = not isReverse
        elif func == "D":
            if arr:
                if isReverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                flag = True
                break
    if flag:
        print("error")
    else:
        if isReverse:
            arr.reverse()
        print("["+",".join(arr)+"]")
