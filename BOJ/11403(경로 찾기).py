import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            for k in range(n):
                if board[j][k] == 1:
                    board[i][k] = 1
                
for i in range(n):
    for j in range(n):
        # i에서 j로 가는길이 있는지 확인한다
        for k in range(n):
            if board[i][k] == 1 and board[k][j] == 1:
                board[i][j] = 1
                break
                
for row in board:
    for element in row:
        print(element, end=" ")
    print("")

# 다른 사람의 더 간단한 풀이
#import sys
#input = sys.stdin.readline
#
#n = int(input())
#board = [list(map(int,input().split())) for _ in range(n)]
#
#for i in range(n):
#    for j in range(n):
#        for k in range(n):
#            if board[j][i] == 1 and board[i][k] == 1:
#                board[j][k] = 1
#
#for row in board:
#    for element in row:
#        print(element, end=" ")
#    print("")
