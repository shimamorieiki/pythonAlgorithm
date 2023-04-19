import re

S = input()

p1 = re.match(r"^k.*eyence$", S)
p2 = re.match(r"^ke.*yence$", S)
p3 = re.match(r"^key.*ence$", S)
p4 = re.match(r"^keye.*nce$", S)
p5 = re.match(r"^keyen.*ce$", S)
p6 = re.match(r"^keyenc.*e$", S)
p7 = re.match(r".*keyence$", S)
p8 = re.match(r"^keyence.*", S)

if any(p is not None for p in [p1, p2, p3, p4, p5, p6, p7, p8]):
    print("YES")
else:
    print("NO")

# AC 10m
# 両端が取得されてしまうのを忘れてた
