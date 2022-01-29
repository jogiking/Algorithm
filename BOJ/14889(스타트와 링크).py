def get_point(g, board):
    total = 0
    for i in g:
        for j in g:
            total += board[i][j]
    return total
    
def get_diff(teams):
    global board
    g1, g2 = [], []
    for i in range(len(teams)):
        if teams[i]:
            g1.append(i)
        else:
            g2.append(i)
    sum_g1 = get_point(g1, board)
    sum_g2 = get_point(g2, board)
    return abs(sum_g1-sum_g2)

def dfs(phase, visited, count):
    global answer
    if count == len(visited)//2:
        answer = min(answer, get_diff(visited))
        return
    for i in range(phase, len(visited)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, visited, count+1)
            visited[i] = False

size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]
answer = 987654321
dfs(0, [False]*size, 0)
print(answer)
