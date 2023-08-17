def f(i, N):
    if i == N:
        s = 0
        for j in range(N):
            if lst2[j]:
                s += lst1[j]
                print(lst1[j],end=' ')
        print(f'   sum : {s}')
        return
    else:
        lst2[i] = lst1[i]
        f(i+1, N)
        lst2[i] = 0
        f(i+1, N)
        return


lst1 = [1,2,3]
lst2 = [0,0,0]

f(0, 3)