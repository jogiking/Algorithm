from collections import Counter
from functools import reduce

r,c,k = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(3)]

# 1)추출하고 2)재정렬해서 3)다시 배열로 완성
def op_r():
    global board
    max_size = 0
    for i in range(len(board)):
        counter = Counter(board[i])
        del counter[0]
        temp = reduce(lambda a,b: a+[b[0],b[1]], sorted(list(counter.items()), key=lambda x: (x[1], x[0])), [])
        board[i] = temp[:100]
        max_size = max(max_size, len(temp))
    for i in range(len(board)):
        for _ in range(max_size-len(board[i])):
            board[i].append(0)
def op_c():
    global board
    new_board = []
    max_size = 0
    for i in range(len(board[0])):
        col = [x[i] for x in board]
        counter = Counter(col)
        del counter[0]
        temp = reduce(lambda a,b: a+[b[0],b[1]], sorted(list(counter.items()), key=lambda x: (x[1], x[0])), [])
        new_board.append(temp[:100])
        max_size = max(max_size, len(new_board[i]))
    for i in range(len(new_board)):
        for _ in range(max_size-len(new_board[i])):
            new_board[i].append(0)
    board = list(map(list,zip(*new_board)))
    
t = 0
while t<=100:
    if r<=len(board) and c<=len(board[0]) and board[r-1][c-1] == k:
        break
    if len(board)>=len(board[0]):
        op_r()
    else:
        op_c()
    t+=1
    
answer = -1 if t>100 else t
print(answer)
