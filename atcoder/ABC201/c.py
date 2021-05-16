s = input()
        
count = 0
for i in range(10000):
    a = "{:04d}".format(i)
    for j in range(10):
        if s[j] == "o" and a.count(str(j)) == 0:
            break
        elif s[j] == "x" and a.count(str(j)) != 0:
            break
    else:
        count+=1
print(count)