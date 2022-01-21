def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i+=1
    return True

def solution(n, k):
    v = n
    
    stack = []
    while v > 0:
        stack.append(v%k)
        v//=k
    conv = "".join(map(str,reversed(stack)))
    splited = list(map(int, filter(lambda x: x!= '', conv.split('0'))))
    
    return len(list(filter(isPrime, splited)))