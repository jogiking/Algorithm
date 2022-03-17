def solution(msg):
    answer = []
    dict = {}
    count = 1
    n = len(msg)
    for ch in "abcdefghijklmnopqrstuvwxyz".upper():
        dict[ch] = count
        count+=1
    
    i = 0
    while i<n:
        j=i+1
        while j<=n and msg[i:j] in dict:
            j+=1
        answer.append(dict[msg[i:j-1]])
        if j<=n:
            if msg[i:j] not in dict:
                dict[msg[i:j]]=count
                count+=1
        i=j-1
    return answer