from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque(list(map(lambda x: (x[0],x[1]), enumerate(priorities))))
    while q:
        i,v1 = q.popleft()
        flag = True
        for j,v2 in q:
            if v1<v2:
                q.append((i,v1))
                flag = False
                break
                
        if flag:
            answer+=1
            if i==location:
                return answer