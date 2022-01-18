def solution(progresses, speeds):
    answer = []
    day = 0
    
    for i in range(len(progresses)):
        if day*speeds[i] + progresses[i] < 100:
            answer.append(0)
            a = max(0, 100-progresses[i]-day*speeds[i])
            b = speeds[i]
            day += (a+b-1)//b
            
        answer[-1] += 1
        
    return answer