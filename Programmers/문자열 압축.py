# 두번째 버전
# 첫번째 반복문 안에서 before의 초기값을 ""으로 바꾸고 두번째 반복문을 두번째에서 첫번째부터 비교하게 수정함.
# 일관적인 반복문의 시작 코드로 개선.

def solution(s):
    size = len(s)
    min_length = size
    for d in range(1, size//2+1):
        before = ""
        length = 0
        count = 1
        for i in range(0, size//d):
            now = s[i*d:(i+1)*d]
            if before == now:
                count += 1
            else:
                if count > 1:
                    length += len(str(count)) + d
                else:
                    length += d
                count = 1
            before = now
            
        if count > 1:
            length += len(str(count)) + d
    
        length += size%d
        min_length = min(length, min_length)
        
    return min_length

# 첫번째 버전
# def solution(s):
#     size = len(s)
#     min_length = size
#     for d in range(1, size//2+1):
#         before = s[0:d]
#         length = 0
#         count = 1
#         for i in range(1, size//d):
#             if before == s[i*d:(i+1)*d]:
#                 count += 1
#             else:
#                 if count > 1:
#                     length += len(str(count)) + d
#                 else:
#                     length += d
#                 count = 1
#             before = s[i*d:(i+1)*d]
            
#         if count > 1:
#             length += len(str(count)) + d
#         else:
#             length += d
#         length += size%d
#         min_length = min(length, min_length)
        
#     return min_length