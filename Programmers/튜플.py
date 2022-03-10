def solution(s):
    answer = []
    s=map(lambda x: set(map(int,x.split(","))), s.strip("{}").split("},{"))
    s= list(s)
    s.sort(key=lambda x:len(x))
    res = set()
    for element in s:
        answer.append(list(element-res)[0])
        res=element
    return answer