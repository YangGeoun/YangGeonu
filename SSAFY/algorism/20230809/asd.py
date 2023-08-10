# arr = [1,2,3,4,5]
# N = 5
# M = 3
# selected = [0] * N
#
#
# def comb(idx, cnt):
#     if cnt == M:
#         print(selected)
#         return
#     if idx == N:
#         return
#     for i in range(2):
#         selected[idx] = i
#         comb(idx+1, cnt+i)
#         selected[idx] = 0
#
# comb(0,0)
print(list(range(0,7,3)))
