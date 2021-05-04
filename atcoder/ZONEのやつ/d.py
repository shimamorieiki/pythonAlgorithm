s = input().split("R")
t = ""

if len(s) %2==0:
    t = s[0][::-1] + s[1]    
    for i in range(2,len(s)-1):
        t = s[i][::-1] + t + s[i+1]
else:
    t = s[0]
    for i in range(1,len(s)-1):
        t = s[i][::-1] + t + s[i+1]

t = [i for i in t]
i = 0
while i < len(t)-1:
    if t[i] == t[i+1]:
        del t[i+1]
        del t[i]
        i = i - 1 if i != 0 else i
    else:
        i +=1
print("".join(t))