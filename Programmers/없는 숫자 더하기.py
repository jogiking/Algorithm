def solution(numbers):
    answer = sum(range(10))
    for n in numbers:
        answer-=n
    return answer