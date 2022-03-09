def get_time(s):
    temp = list(map(int,s.split(":")))
    res = 0
    res += temp[0]*3600
    res += temp[1]*60
    res += temp[2]
    res *= 1000
    res += temp[3]
    return res
    
def parse(s1,s2):
    temp = s1.split()
    end = get_time(temp[0].replace(".",":"))
    duration = int(float(s2[:-1])*1000)
    start = end-duration+1
    return start,end

def solution(lines):
    answer = 0
    lines = list(map(lambda x: parse(x[0],x[1]), map(lambda x: x.split()[1:], lines)))
    for i in range(len(lines)):
        _, current_end = lines[i]
        count = 0
        for j in range(i,len(lines)):
            start, _ = lines[j]
            if start - 1000 < current_end:
                count += 1
        answer = max(answer, count)
    return answer