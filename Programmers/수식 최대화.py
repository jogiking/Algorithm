# 두번째 방법
# 정규식 연산을 사용해서 숫자와 연산자를 각각 분리.
# eval 함수를 사용하여 연산수행, 이때 우선순위 순으로 각 연산자를 먼저나온순으로 수행한다.
# 첫번쨰 방법은 중위 표현식을 후위 표현식으로 바꿔 계산을 해나가는, 정석적인 방법이고,
# 두번째 방법은 좀 더 간단한 방법으로, 연산자 배열의 인덱스와 피연산자 인덱스 차이가 1이 차이난다는 특징을 이용했다.

import re
def solution(expression):
    answer = -1
    combinations = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    for combination in combinations:
        operands = re.split('[*+-]',expression)
        operators = re.split('[0-9]+',expression)[1:-1]
        for op in combination:
            k = 0
            while k < len(operators):
                if op == operators[k]:
                    operands[k] = str(eval(operands[k]+op+operands[k+1]))
                    del operators[k]
                    del operands[k+1]
                else:
                    k+=1
        answer = max(answer, abs(int(operands[0])))
    return answer

# 첫번째 방법
#
# from functools import reduce
# from itertools import permutations

# def split_expression(s):
#     ops = []
#     nums = []
#     arr = list(s)
#     for i, ch in enumerate(arr):
#         if not ch.isdecimal():
#             ops.append(ch)
#             arr[i] = " "
#     nums = "".join(arr).split()
#     return list(reduce(lambda a,b: a+b, zip(nums,ops)))+[nums[-1]]

# def make_postfix(arr, priority):
#     res = []
#     ops = []
#     for ch in arr:
#         if ch.isdecimal():
#             res.append(ch)
#         else:
#             while ops:
#                 if priority.index(ops[-1]) > priority.index(ch):
#                     break
#                 res.append(ops.pop())
#             ops.append(ch)
#     while ops:
#         res.append(ops.pop())
#     return res

# def calculate_postfix(arr):
#     values = []
#     for ch in arr:
#         if ch.isdecimal():
#             values.append(int(ch))
#         else:
#             rhs, lhs = values.pop(), values.pop()
#             if ch == "*":
#                 values.append(lhs*rhs)
#             elif ch == "+":
#                 values.append(lhs+rhs)
#             elif ch == "-":
#                 values.append(lhs-rhs)
#     return values[0]
                
# def solution(expression):
#     answer = -1
#     splited = split_expression(expression)
#     for priority in permutations("*+-", 3):
#         postfix = make_postfix(splited, priority)
#         value = abs(calculate_postfix(postfix))
#         answer = max(value, answer)
#     return answer