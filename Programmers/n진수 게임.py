def conv(n, a): # n진법, 십진수 숫자 a를 변환
    mapper = list("0123456789ABCDEF")
    q = a
    res = []
    if a<1:
        return ["0"]
    while q > 0:
        res.append(mapper[q%n])
        q//=n
    return res
    
def solution(n, t, m, p):
    idx = 0
    num = 0
    answer = []
    while True:
        res = conv(n, num)
        for i in range(idx,idx+len(res)):
            if i%m+1==p:
                answer.append(res[-(i-idx+1)])
                if len(answer)==t:
                    return "".join(answer)
        num+=1
        idx+=len(res)