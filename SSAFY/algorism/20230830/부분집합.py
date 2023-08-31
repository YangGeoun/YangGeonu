def subset(i):
    if i == N:
        ans.append(temp[:])
    else:
        temp[i] = lst[i]
        subset(i+1)
        temp[i] = 0
        subset(i+1)


def comb(i,k):
    if k == 2:
        ans.append(temp[:])
        return
    elif i == N:
        return
    else:
        comb(i+1,k)
        temp[i] = lst[i]
        comb(i+1,k+1)
        temp[i] = 0
        return


N = 4
lst = [i+1 for i in range(N)]
temp = [0] * N
ans = []
comb(0,0)
for el in ans:
    print(el)