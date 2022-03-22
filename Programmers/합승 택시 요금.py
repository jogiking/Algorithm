def solution(n, s, a, b, fares):
    INF = 1e9
    board = [[INF]*(n+1) for _ in range(n+1)]
    for start,end,v in fares:
        board[start][end]=v
        board[end][start]=v
    
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if i==j:
                    board[i][j]=0
                else:
                    board[i][j] = min(board[i][j], board[i][k]+board[k][j])
    
    answer = INF
    for x in range(1,n+1):
        answer = min(board[s][x]+board[x][a]+board[x][b], answer)
        
    return answer