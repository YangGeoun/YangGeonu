def f(i, N, s, t):        # i-1원소까지 부분집합의 합(포함된 원소의 합)
    if s > t:
        return
    if s == t:
        s = 0
        for j in range(N):
            if lst2[j]:
                s += lst1[j]
                print(lst1[j], end=' ')
        print(f'   sum : {s}')
        return
    print('*')
    if i == N:
        return
    else:
        lst2[i] = lst1[i]
        f(i+1, N, s+lst1[i], t)  # 부분집합에 lst1[i] 포함
        lst2[i] = 0
        f(i+1, N, s, t)          # 부분집합에 lst1[i] 빠짐
        return


lst1 = [1,2,3,4]
lst2 = [0,0,0,0]

f(0, 4, 0, 3)