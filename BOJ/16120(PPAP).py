s = list(input())
def solution():
    count = 0
    i = 0
    while i < len(s):
        if s[i]=="A":
            if i+1<len(s) and count>=2 and s[i+1] == "P":
                count-=1
                i+=2
            else:
                print("NP")
                return
        elif s[i]=="P":
            count+=1
            i+=1

    if count == 1:
        print("PPAP")
    else:
        print("NP")

solution()
