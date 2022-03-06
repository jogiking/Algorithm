from itertools import permutations
from functools import reduce

def isPrime(n):
    i=2
    if n<2:
        return False
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
        
def solution(numbers):
    nums = list(map(int,numbers))
    s = set()
    for i in range(1,len(nums)+1):
        for element in permutations(nums,i):
            s.add(reduce(lambda a,b: 10*a+b, element, 0))
                
    return len([x for x in s if isPrime(x)])