def conv(s):
    h,m=list(map(int,s.split(":")))
    return h*60 + m

def conv_to_str(n):
    h = n//60
    m = n%60
    res = str(h).zfill(2)+":"+str(m).zfill(2)
    return res
    
def solution(n, t, m, timetable):
    time = list(map(conv, timetable))
    time.sort()
    group = []
    count = 0
    boundary = 9*60
    for i in range(n):
        temp = []
        for _ in range(m):
            if count>=len(time):
                break
            if time[count]>boundary:
                break
            temp.append(time[count])
            count+=1
        group.append(temp)
        boundary+=t
        
    if len(group[-1]) < m:
        return conv_to_str(60*9+(n-1)*t)
    else:
        return conv_to_str(group[-1][:m][-1]-1)