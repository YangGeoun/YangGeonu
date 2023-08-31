def f(i, N):
    if i == N:
        print(p)
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = temp[j]
                used[j] = 1
                f(i+1,N)
                used[j] = 0


def f2(i, N, K):
    if i == K:
        print(p)
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                f2(i+1,N,K)
                used[j] = 0


temp = [2,3,4]


#
# K = 3
# card = list(map(int, input()))
used = [0] * 6
p = [0] * 3
# f2(0,6,3)
f(0,3)