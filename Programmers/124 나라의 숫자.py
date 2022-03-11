def solution(n):
    answer = ''
    stack = []
    q = n
    while q>0:
        r = q%3
        if r==0:
            stack.append("4")
            q=q//3-1
        else:
            stack.append(str(r))
            q//=3
    
    answer = "".join(reversed(stack))
    return answer