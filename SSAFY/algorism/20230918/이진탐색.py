def solve(l, r, tg, x):
    if l > r:
        return 0
    mid = (l+r) // 2
    if arr1[mid] == tg:
        return 1
    elif arr1[mid] > tg:
        if x == 1:
            return 0
        return solve(l, mid-1, tg, 1)
    else:
        if x == 2:
            return 0
        return solve(mid + 1, r, tg, 2)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr1.sort()
    arr2 = list(map(int, input().split()))
    cnt = 0
    for el in arr2:
        if solve(0, N-1, el, 0):
            cnt += 1
    print(f'#{tc} {cnt}')