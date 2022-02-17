n,k = list(map(int,input().split()))
goods = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for w in range(1,k+1):
        if w < goods[i-1][0]:
            dp[i][w] = dp[i-1][w]
        else:
            if dp[i-1][w] > dp[i-1][w-goods[i-1][0]]+goods[i-1][1]:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w-goods[i-1][0]]+goods[i-1][1]
print(dp[-1][-1])
