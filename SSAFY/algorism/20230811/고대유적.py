T = int(input())

for tc in range(1, T +1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        cnt = 0
        max_cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if max_cnt < cnt:
                max_cnt = cnt
        if ans < max_cnt:
            ans = max_cnt

    for j in range(M):
        cnt = 0
        max_cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if max_cnt < cnt:
                max_cnt = cnt
        if ans < max_cnt:
            ans = max_cnt

    print(f'#{tc} {ans}')