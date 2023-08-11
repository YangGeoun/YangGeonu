N, K = map(int, input().split())

lst = [i+1 for i in range(N)]
ans = []
n = 0
while lst:
    del_lst = []
    for i in range(len(lst)):
        n += 1
        if n % K == 0:
            del_lst.append(lst[i])
    for el in del_lst:
        lst.remove(el)
        ans.append(el)
print(ans)


