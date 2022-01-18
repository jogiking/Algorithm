def solution(numbers, target):
    answer = 0
    size = len(numbers)
    path = [0]*size

    def dfs(phase):
        nonlocal size, answer
        if phase >= size:
            if sum(path) == target:
                answer += 1
            return
        
        path[phase] = numbers[phase]
        dfs(phase+1)
        path[phase] *= -1
        dfs(phase+1)
    
    dfs(0)
     
    return answer