n = int(input())
dict = {}
for _ in range(n):
    sc = 1
    for key in reversed(list(input())):
        if key not in dict:
            dict[key] = sc
        else:
            dict[key] += sc
        sc*=10
num = 9
answer = 0
for v in sorted(dict.values(), reverse=True):
    answer += num*v
    num-=1
    
print(answer)
