from collections import Counter

def make_all_candidates(s):
    res = []
    for i in range(len(s)-1):
        res.append(s[i:i+2].upper())
    return res

def filter_candidates(arr):
    return list(filter(lambda x: x.isalpha(), arr))
    
def solution(str1, str2):
    answer = 0
    
    c1 = Counter(filter_candidates(make_all_candidates(str1)))
    c2 = Counter(filter_candidates(make_all_candidates(str2)))
    
    intersection = {}
    union = c1.copy()
    for word, count in c2.items():
        if word in c1:
            union[word] = max(count, union[word])
        else:
            union[word] = count
    
    for word, count in c1.items():
        if word in c2:
            intersection[word] = min(count, c2[word])

    union_size = sum(union.values())
    intersection_size = sum(intersection.values())
    
    if union_size == 0:
        return 1*65536
    else:
        return int(intersection_size/union_size*65536)