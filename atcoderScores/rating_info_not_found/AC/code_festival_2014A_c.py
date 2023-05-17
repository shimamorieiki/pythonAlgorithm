# 頑張って余りを計算するだけ

A,B = map(int,input().split(" "))

a4_div,a4_mod = divmod(A,4)
b4_div,b4_mod = divmod(B,4)
a100_div,a100_mod = divmod(A,100)
b100_div,b100_mod = divmod(B,100)
a400_div,a400_mod = divmod(A,400)
b400_div,b400_mod = divmod(B,400)

n4 = b4_div - (a4_div+min(1,a4_mod)) + 1

n100 = b100_div - (a100_div+min(1,a100_mod)) + 1

n400 = b400_div - (a400_div+min(1,a400_mod)) + 1

print(n4 - n100 + n400)

# AC 10