def perm(idx):
    global cnt, ans
    if idx == N//2:
        sum = 0
        for el in perm_arr:
            sum += abs(el)
        if sum <= N//2:
            # print(perm_arr)
            di, dj = perm_arr
            ans += int(arr[N // 2 + di][N // 2 + dj])
            cnt += 1
            return
        else:
            return
    for i in range(N):
        perm_arr[idx] = a[i]
        perm(idx+1)


T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = [input() for _ in range(N)]
    M = N // 2
    perm_arr = [0] * (N//2)
    a = [-(N//2) + i for i in range(N)]
    ans = 0
    perm(0)
    print(ans)