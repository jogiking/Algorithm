s = input()[:-1].split()
for i in range(1,len(s)):
    print(s[0],end="")
    count=0
    for index, element in enumerate(s[i][-1::-1]):
        if element == ",":
            continue
        elif element == "[":
            print("]",sep="",end="")
        elif element == "]":
            print("[",sep="",end="")
        elif element == "*" or element == "&":
            print(element,sep="",end="")
        else:
            print(" %s;"%s[i][:len(s[i])-index])
            break
