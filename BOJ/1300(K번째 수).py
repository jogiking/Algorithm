n = int(input())
k = int(input())

# 내가 찾는 순서가 6이라면?
# 숫자 4: 4보다 같거나 작은 수의 개수가 6개가  있다는 소리
left = 1
right = n*n
while left<right:
    mid = (left+right)//2
    temp = 0
    for y in range(1,n+1):
        temp += min(mid//y, n)
    if temp>=k:
        right = mid
    elif temp<k:
        left = mid+1
        answer = left
        
print(left)
