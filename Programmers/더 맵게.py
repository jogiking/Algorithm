import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    q = scoville
    while len(q)>=2:
        a = heapq.heappop(q)
        if a>=K:
            return answer
        b = heapq.heappop(q)
        heapq.heappush(q,a+2*b)
        answer+=1
    
    return answer if q[0]>=K else -1