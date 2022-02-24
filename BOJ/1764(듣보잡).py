n,m = list(map(int,input().split()))
set_a = set([input() for _ in range(n)])
set_b = set([input() for _ in range(m)])
intersection = set_a&set_b
print(len(intersection))
for element in sorted(intersection):
    print(element)
