def solution(answers):
    temp = [[1,0],[2,0],[3,0]]
    for i in range(len(answers)):
        if answers[i] == i%5+1:
            temp[0][-1]+=1
        
        if i%2==0:
            if answers[i]==2:
                temp[1][-1]+=1
        else:
            pattern = [1,3,4,5]
            if answers[i] == pattern[(i//2)%4]:
                temp[1][-1]+=1
        
        pattern = [3,1,2,4,5]
        if answers[i] == pattern[(i//2)%5]:
            temp[2][-1]+=1
    
    answer = []
    res = list(sorted(temp,key=lambda x: -x[-1]))
    max_value = res[0][-1]

    for i, v in list(sorted(temp,key=lambda x: -x[-1])):
        if max_value == v:
            answer.append(i)
    
    return answer