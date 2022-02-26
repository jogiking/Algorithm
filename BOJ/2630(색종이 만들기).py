n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer = [0,0]
def div_conq(y,x,n):
    temp = board[y][x]
    flag = False
    for i in range(n):
        if flag:
            break
        for j in range(n):
            if board[y+i][x+j] == temp:
                temp = board[y+i][x+j]
            else:
                flag = True
                break

    if not flag:
        answer[temp]+=1
        return

    div_conq(y, x, n//2)
    div_conq(y, x+n//2, n//2)
    div_conq(y+n//2, x, n//2)
    div_conq(y+n//2, x+n//2, n//2)

div_conq(0,0,n)
for element in answer:
    print(element)
