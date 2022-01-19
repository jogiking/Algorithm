# 두번째 방법(이분탐색)
# N은 info의 크기, M은 query의 크기
# Time: O(N*NlogN + MlogN) = O(logN(N^2 + M))
# 모든 경우의 수를 만들 때 info의 크기마다 정렬 => N*NlogN 
# 매 query마다 이분탐색 => MlogN
# N <= 50000, M <= 100000

from itertools import combinations
from bisect import bisect_left

def make_all_cases(info):
    res = []
    for i in range(len(info) + 1):
        cases = list(combinations(info, i))
        for case in cases:
            res.append("".join(case))
    return res

def extract_from_query(query):
    splited = query.split()
    res = []
    for element in splited:
        if element != "and" and element != "-":
            res.append(element)
    return ("".join(res[:-1]), int(res[-1]))


def solution(info, query):
    answer = []
    info_dict = {}
    for row in info:
        info_splited = row.split()
        cases = make_all_cases(info_splited[:4])
        point = int(info_splited[-1])
        for case in cases:
            if case not in info_dict:
                info_dict[case] = [point]
            else:
                info_dict[case].append(point)

    # 이분 탐색을 위한 정렬
    for key in info_dict:
        info_dict[key].sort()

    for row in query:
        q, point = extract_from_query(row)
        
        # 요청한 쿼리에 해당하는 데이터가 없는 경우
        if q not in info_dict:
            answer.append(0)
        else:
            candidates = info_dict[q]
            pos = bisect_left(candidates, point)
            answer.append(len(candidates) - pos)

    return answer

# 첫번쨰 방법(전체탐색) -> 시간초과
# N은 info의 크기, M은 query의 크기
# Time: O(N*M)
# 매 쿼리를 돌면서 조건에 맞는지 확인하는 방법