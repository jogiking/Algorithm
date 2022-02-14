x,y = list(map(int,input().split()))
origin = (100*y)//x

def decision(n):
    return (100*(y+n))//(x+n) > origin

if origin >= 99:
    print(-1)
else:
    left = 1
    right = x
    while left<right:
        mid = (left+right)//2
        if decision(mid):
            right = mid
        else:
            left = mid+1
    print(left)
