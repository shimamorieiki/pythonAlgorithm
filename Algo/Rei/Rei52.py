import queue

# q = queue.Queue()
# for i in range(5):
#     q.put(i)
# print(list(q.queue))
# while not q.empty():
#     print(q.get())


N = 8
a = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0],
        [0,1,0,1,1,1,0,0,0],
        [0,0,1,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,1,1],
        [0,0,0,1,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,0]
    ]

v = [0]*(N+1)
q = queue.Queue()
q.put(1)
v[1] = 1

while not q.empty():
    i =  q.get()
    for j in range(N+1):
        if a[i][j]==1 and v[j]==0:
            print(i,"=>",j," ",end="")
            q.put(j)
            v[j] = 1
print("\n")