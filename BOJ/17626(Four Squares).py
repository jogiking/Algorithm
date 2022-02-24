# 같은 수를 두번 사용하는 경우도 포함시켜야 했다.

n = int(input())
cache = set()
i=1
while True:
    temp = i*i
    if temp>n:
        break
    cache.add(temp)
    i+=1

def solution(target):
    if n in cache:
        return 1
    history = sorted(cache, reverse=True)
    for element in history:
        if target-element in cache:
            return 2

    for i in range(len(history)):
        for j in range(len(history)):
            temp = history[i]+history[j]
            if temp > target:
                continue
            if target-temp in cache:
                return 3
    return 4
    
print(solution(n))
            
