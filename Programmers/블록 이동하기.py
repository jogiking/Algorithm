from collections import deque

def make_candidate(p1,p2,board):
    cand = []
    n = len(board)
    # 상하좌우
    for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
        np1=(p1[0]+dy,p1[1]+dx)
        np2=(p2[0]+dy,p2[1]+dx)
        if np1[0]<0 or np1[0]>=n or np1[1]<0 or np1[1]>=n:
            continue
        if np2[0]<0 or np2[0]>=n or np2[1]<0 or np2[1]>=n:
            continue
        if board[np1[0]][np1[1]]==1 or board[np2[0]][np2[1]]==1:
            continue
        cand.append((np1,np2))
        
    # 회전
    if p1[0]==p2[0]: # 가로방향일 때
        for dy,dx in (1,0),(-1,0):
            np1=(p1[0]+dy,p1[1]+dx)
            np2=(p2[0]+dy,p2[1]+dx)
            if np1[0]<0 or np1[0]>=n or np1[1]<0 or np1[1]>=n:
                continue
            if np2[0]<0 or np2[0]>=n or np2[1]<0 or np2[1]>=n:
                continue
            if board[np1[0]][np1[1]]==0 and board[np2[0]][np2[1]]==0:
                cand.append((p1,np1))
                cand.append((p2,np2))
    else: # 세로방향일 때
        for dy,dx in (0,1),(0,-1):
            np1=(p1[0]+dy,p1[1]+dx)
            np2=(p2[0]+dy,p2[1]+dx)
            if np1[0]<0 or np1[0]>=n or np1[1]<0 or np1[1]>=n:
                continue
            if np2[0]<0 or np2[0]>=n or np2[1]<0 or np2[1]>=n:
                continue
            if board[np1[0]][np1[1]]==0 and board[np2[0]][np2[1]]==0:
                cand.append((np1,p1))
                cand.append((np2,p2))
    return cand
    
def solution(board):
    visited = set([(0,0),(0,1)])
    q = deque([((0,0),(0,1),0)])
    n = len(board)
    while q:
        p1,p2,v = q.popleft()
        if p1==(n-1,n-1) or p2==(n-1,n-1):
            return v
        for element in make_candidate(p1,p2,board):
            if element not in visited:
                visited.add(element)
                q.append((*element,v+1))