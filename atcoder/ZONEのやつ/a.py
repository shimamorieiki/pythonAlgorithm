s = input()
count = 0
while s.find("ZONe") >= 0:
    count +=1
    s = s[s.find("ZONe")+1:]
print(count)