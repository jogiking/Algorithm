n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer = [0,0,0]
def check(y1,x1,y2,x2):
    prev = board[y1][x1]
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            if board[y][x] != prev:
                return False
            prev = board[y][x]
    return True

def req(y1,x1,y2,x2):
    if check(y1,x1,y2,x2):
        answer[board[y1][x1]+1]+=1
        return
    size = (y2-y1+1)//3
    req(y1,x1,size+y1-1,size+x1-1)
    req(y1,size+x1,size+y1-1,2*size+x1-1)
    req(y1,2*size+x1,size+y1-1,3*size+x1-1)

    req(size+y1,x1,2*size+y1-1,size+x1-1)
    req(size+y1,size+x1,2*size+y1-1,2*size+x1-1)
    req(size+y1,2*size+x1,2*size+y1-1,3*size+x1-1)

    req(2*size+y1,x1,3*size+y1-1,size+x1-1)
    req(2*size+y1,size+x1,3*size+y1-1,2*size+x1-1)
    req(2*size+y1,2*size+x1,3*size+y1-1,3*size+x1-1)

req(0,0,n-1,n-1)
for element in answer:
    print(element)
