def solution(x):
    total = 0
    _x = x
    while _x != 0:
        total+=_x%10
        _x//=10
        
    return x%total == 0