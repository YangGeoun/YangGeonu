def subset(i):
    if i == N:
        if sum(temp) == 0:
            ans.append(temp[:])
    else:
        temp[i] = lst[i]
        subset(i+1)
        temp[i] = 0
        subset(i+1)


lst = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(lst)
temp = [0] * N
ans = []
subset(0)
print(ans)