from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for i in range(1,len(dungeons)+1):
        for element in permutations(dungeons, i):
            origin = k
            cnt = 0
            for min_piro, need_piro in element:
                if origin >= min_piro and origin - need_piro >= 0:
                    cnt += 1
                    origin -= need_piro
                else:
                    break        
            answer = max(answer, cnt)
    return answer
