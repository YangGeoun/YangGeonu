T = int(input())
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = 2
    for i in range(M):
        x, y, z = map(int, input().split())
        a = 0
        if z == 1:
            a = 2
        else:
            a = 1
        arr[x-1][y-1] = z
        for d in range(8):
            cnt = 0
            ni = x + di[d] - 1
            nj = y + dj[d] - 1
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == a:
                for n in range(1, N):
                    cnt += 1
                    ni = x + n * di[d] - 1
                    nj = y + n * dj[d] - 1
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == z:
                            x2 = x - 1 + di[d]
                            y2 = y - 1 + dj[d]
                            for dd in range(cnt-1):
                                arr[x2][y2] = z
                                x2 = x2 + di[d]
                                y2 = y2 + dj[d]
                            break
    b = 0
    w = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                b += 1
            elif arr[i][j] == 1:
                w += 1
    print(f'#{tc}',w,b)