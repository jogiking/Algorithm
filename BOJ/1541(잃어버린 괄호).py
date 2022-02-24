s=input()
op=[]
for i in range(len(s)):
    if not s[i].isdigit():
        op.append(s[i])
        s=s.replace(s[i],' ',1)
s=list(map(int, s.split()))

i=0
while '+' in op:
    if op[i]=='+':
        s[i]+=s[i+1]
        s.pop(i+1)
        op.pop(i)
        i=0
    else:
        i+=1
result=s[0]
for i in range(1,len(s)):
    result-=s[i]
print(result)
