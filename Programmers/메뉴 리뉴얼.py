# 두번째 방법
# 첫번째 방법에서는 데이터 가공을 위해 각 단계를 분리했음
# 또 분리하는 방법에서, 후보군을 만들 때 각 orders끼리 비교하는 방법을 선택했는데, 이 부분에서 코드의 복잡성이 증가함
# 두번째 방법에서는 이 부분을 각 order끼리 비교하는 것이 아니라 각각 order마다 확인하는 방법으로 변경했고 이 결과롤 코드가 간단해짐
# 문제가 잘 읽히지 않아서 이해하는데 시간이 걸렸다.

from itertools import combinations
def solution(orders, course):
    answer = []
    for k in course:
        count_dict = {}
        best_selled = (0, [])
        for order in orders:
            for menu in list(map("".join, map(sorted, combinations(order, k)))):
                if menu not in count_dict:
                    count_dict[menu] = 1
                else:
                    count_dict[menu] += 1
        for menu, count in count_dict.items():
            if count > 1:
                if best_selled[0] < count:
                    best_selled = (count , [menu])
                elif best_selled[0] == count:
                    best_selled[1].append(menu)
        
        if best_selled[1]:
            answer += best_selled[1]
    answer.sort()
        
    return answer

# 실패한 코드(정확도)
# from itertools import combinations
# def solution(orders, course):
#     order_length = len(orders)
#     words = set()
#     for i in range(order_length-1):
#         for j in range(i+1, order_length):
#             intersection = "".join(set(orders[i])&set(orders[j]))
#             l = len(intersection)
#             if l<2:
#                 continue
#             words.add(intersection)
#     for word in list(words):
#         length = len(word)
#         for n in course:
#             if length>n:
#                 combi = combinations(word, n)
#                 words|=set(list(map(lambda x: "".join(x), combi)))
#     frequency = dict.fromkeys(words, 0)
#     for key in frequency:
#         for order in orders:
#             if set(key).issubset(set(order)):
#                 frequency[key]+=1
#     temp = {}
#     for key, fre in frequency.items():
#         length = len(key)
#         if length in temp:
#             if temp[length][0] < fre:
#                 temp[length] = (fre, [key])
#             elif temp[length][0] == fre:
#                 temp[length][1].append(key)
#         else:
#             temp[length] = (fre, [key])
#     answer = []
#     for n in course:
#         if n in temp:
#             answer+=temp[n][1]
#     for i in range(len(answer)):
#         answer[i] = "".join(sorted(answer[i]))
#     answer.sort()
#     return answer