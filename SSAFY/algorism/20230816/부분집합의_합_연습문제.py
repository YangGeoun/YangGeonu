def f(i, N):           # 2047번 호출
    global num
    num += 1
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


def f2(i, N, s, t):        # i-1원소까지 부분집합의 합(포함된 원소의 합)
    global num             # 349번 호출
    num += 1
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

    if i == N:
        return
    else:
        lst2[i] = lst1[i]
        f2(i+1, N, s+lst1[i], t)  # 부분집합에 lst1[i] 포함
        lst2[i] = 0
        f2(i+1, N, s, t)          # 부분집합에 lst1[i] 빠짐
        return


num = 0
N = 10
lst1 = [i+1 for i in range(N)]
lst2 = [0] * N

# f(0, N)
f2(0, N, 0, 10)
print(num)