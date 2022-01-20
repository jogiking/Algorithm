def isBalance(s):
    return s.count("(") == s.count(")")

def isCorrect(s):
    if not isBalance(s):
        return False
    count = 0
    for element in s:
        if element == "(":
            count+=1
        else:
            count-=1
        if count < 0:
            return False
    return True

def divide(s):
    for i in range(len(s)):
        if isBalance(s[:i+1]):
            return (s[:i+1], s[i+1:])
    return ([], s)

def recur(w):
    if not w:
        return []
    u, v = divide(w)
    if isCorrect(u):
        return u+recur(v)
    else:
        reverse_u = list(map(lambda x: ")" if x=="(" else "(", u))
        return ["("]+recur(v)+[")"]+reverse_u[1:-1]

def solution(p):
    answer = "".join(recur(list(p)))
    return answer