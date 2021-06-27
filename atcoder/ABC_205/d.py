def bisearch(sorted_list,search_value,start):
    left_index: int = 0
    right_index: int = len(sorted_list) - 1
    max_value = max(sorted_list)
    if search_value > start:
        return 0
        
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = sorted_list[middle_index]
        middle_value_plus1: int = sorted_list[middle_index+1]
        # if search_value < middle_value:
        #     right_index = middle_index - 1
        #     continue
        # if search_value > middle_value:
        #     left_index = middle_index + 1
        #     continue

        if middle_value <= search_value and search_value < middle_value_plus1:
            return middle_index
        elif search_value < middle_value:
            right_index = middle_index - 1
        elif search_value > middle_value:
            left_index = middle_index + 1

N,Q= map(int,input().split(" "))
A = list(map(int,input().split(" ")))
K = []
NList = [0]*100001
for i in range(Q):
    K.append(int(input()))
count =1
for i in A:
    if count != i:
        break
    else:
        count+=1
start = count #検索開始位置
print("start",start)
# print(start -1+ K[0] - bisearch(A,K[0]))
# 二分探索でインデックスの値を出してそこまでで計算するのが可能性高そう。
# 二分探索でN[i] <= Q < N[i+1]になるiが分かれば多分解けそう。

# NList = list(set(NList))

for i in K:
    print(i,bisearch(A,i,start))
    print(start -1 + i - bisearch(A,i,start))