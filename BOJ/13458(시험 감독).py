places = int(input())
students = list(map(int, input().split()))
b, c = list(map(int, input().split()))

ans = places
for element in students:
    ans+=(max(element-b, 0)+(c-1))//c
print(ans)
