# 구체적으로는 특정 경우 어떻게 처리해야할지에 대해서 파악을 하는데 시간이 많이 걸렸다.
# 테스트 케이스가 4개나 있었고 각각 설명이 잘 되어있었는데, 아마 충분한 설명이 없었다면 풀지 못했을 것 같다.
# 테스트 케이스를 직접 만들고 이 경우 어떻게 해야하는지 생각하는 연습을 해야겠다.

def calculate_arrays(lhs, rhs):
    lhs_value, rhs_value = 0, 0
    for v1, v2, score in zip(lhs, rhs, reversed(range(11))):
        if v1 > 0 or v2 > 0:
            if v1 >= v2:
                lhs_value += score
            else:
                rhs_value += score
    return lhs_value, rhs_value

def compare_arrays(lhs, rhs):
    for i in reversed(range(len(lhs))):
        v1, v2 = lhs[i], rhs[i]
        if v1 == 0 and v2 == 0:
            continue
        if v1 > v2:
            return lhs
        elif v2 > v1:
            return rhs

def dfs(i, remains, arr, all_cases):
    if i == len(arr) - 1:
        arr[-1] = remains
        all_cases.append(arr[:])
        return
    for j in reversed(range(remains + 1)):
        arr[i] = j
        dfs(i + 1, remains - j, arr, all_cases)

def solution(n, info):
    answer = [-1]

    all_cases = []
    arr = [0] * len(info)
    max_diff = -1
    dfs(0, n, arr, all_cases)
    for case in all_cases:
        v1, v2 = calculate_arrays(info, case)
        if v1 < v2:
            if v2 - v1 > max_diff:
                answer = case
                max_diff = v2 - v1
            elif v2 - v1 == max_diff:
                answer = compare_arrays(answer, case)
        
    return answer