def pop_blocks(row, col, board):      
    need_to_remove = set()
    
    for y in range(row-1):
        for x in range(col-1):
            if board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1] != "@":
                need_to_remove |= set([(y,x), (y,x+1), (y+1,x), (y+1,x+1)])

    for (y,x) in need_to_remove:
        board[y].append("@")
        board[y][x] = "0"
        
    for y in range(row):
        board[y] = [value for value in board[y] if value != "0"]
        
    return len(need_to_remove)

def solution(m, n, board):
    answer = 0
    rotated_board = list(map(list,zip(*board[::-1])))

    while True:
        res = pop_blocks(n,m,rotated_board)
        answer += res
        if res == 0:
            break
            
    return answer