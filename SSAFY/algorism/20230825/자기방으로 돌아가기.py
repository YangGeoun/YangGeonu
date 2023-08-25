T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [0] * 401
    for i in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        if not (s % 2):
            s -= 1
        if not (e % 2):
            e -= 1
        for j in range(s, e+1,):
            arr[j] += 1
    max_v = 0
    for el in arr:
        if max_v < el:
            max_v = el
    print(f'#{tc} {max_v}')