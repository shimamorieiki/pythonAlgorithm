# なんか急に集中が切れたのでいったんおわる

# import queue

# N = 8
# a = [
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,1,0,0,0,0,0],
#         [0,1,0,0,0,1,0,0,0],
#         [0,0,0,0,1,0,0,0,0],
#         [0,0,0,0,0,1,0,0,0],
#         [0,0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,0,0,0,1],
#         [0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,0]
#     ]

# v = [0]*(N+1)

# def visit(i):
#     global v
#     v[i]=1
#     for j in range(1,N+1):
#         if a[i][j]==1 and v[j]==0:
#             visit(j)
#     lq.put(i)

# q = queue.Queue()
# lq = queue.LifoQueue()
# for i in range(1,N+1):
#     if v[i]==0:
#         visit(i)
# print(list(reversed(lq.queue)))