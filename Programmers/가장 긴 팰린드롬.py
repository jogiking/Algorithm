# def solution(s):
#     answer = 1
#     n = len(s)
#     for i in range(n):
#         for j in range(i+1,n):
#             sub_s = s[i:j+1]
#             if sub_s == sub_s[::-1]:
#                 answer = max(answer, j-i+1)
#     return answer

def solution(s):
    answer = 1
    s = list(s)
    n = len(s)
    for i in range(n):
        for j in range(i+1,n):
            if j-i+1 < answer:
                continue
            size = 0 if (j-i+1)%2==0 else 1
            t = 0
            for t in range((j-i+1)//2):
                if s[i+t] != s[j-t]:
                    break
                size+=2
            if size == j-i+1:
                answer = max(answer, size)
    return answer