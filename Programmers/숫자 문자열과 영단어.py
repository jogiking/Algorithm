def solution(s):
    dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    for key, value in dict.items():
        answer = answer.replace(key, value)
    return int(answer)

# 첫번째 버전
# def solution(s):
#     answer = 0
#     i = 0
#     size = len(s)
#     while i < size:
#         if s[i].isdecimal():
#             answer = answer*10 + int(s[i])
#             i+=1
#         else:
#             if s[i] == "z":
#                 i+=4
#                 answer = answer*10
#             elif s[i] == "o":
#                 i+=3
#                 answer = answer*10 + 1
#             elif s[i] == "t": #2,3
#                 if s[i+1] == "w":
#                     i+=3
#                     answer = answer*10 + 2
#                 else:
#                     i+=5
#                     answer = answer*10 + 3
#             elif s[i] == "f": #4,5
#                 if s[i+1] == "o":
#                     i+=4
#                     answer = answer*10 + 4
#                 else:
#                     i+=4
#                     answer = answer*10 + 5
#             elif s[i] == "s": #6,7
#                 if s[i+1] == "i":
#                     i+=3
#                     answer = answer*10 + 6
#                 else:
#                     i+=5
#                     answer = answer*10 + 7
#             elif s[i] == "e":
#                 i+=5
#                 answer = answer*10 + 8
#             elif s[i] == "n":
#                 i+=4
#                 answer = answer*10 + 9
#     return answer