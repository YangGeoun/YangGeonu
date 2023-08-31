import math

def solve(i, N):
    if i == N:
        lst.append(temp[:])
        return
    else:
        for j in range(0, N):
            if j not in temp:
                temp.append(j)
                solve(i+1, N)
                temp.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    spots = list(map(int, input().split()))
    spot = []
    for i in range(4, 2*N+4, 2):
        spot.append((spots[i], spots[i+1]))
    temp = []
    lst = []
    solve(0,N)
    min_v = 9999999
    # for el in lst:
    #     sum_v = 0
    #     x1, y1 = spots[0], spots[1]
    #     x2, y2 = spot[0]
    #     sum_v += abs(x1 - x2) + abs(y1 - y2)
    #     for i in range(len(el)-1):
    #         x1, y1 = spot[el[i]]
    #         x2, y2 = spot[el[i+1]]
    #         distance = abs(x1 - x2) + abs(y1 - y2)
    #         sum_v += distance
    #     x1, y1 = spots[2], spots[3]
    #     sum_v += abs(x1 - x2) + abs(y1 - y2)
    #     if min_v > sum_v:
    #         min_v = sum_v
    print(min_v)