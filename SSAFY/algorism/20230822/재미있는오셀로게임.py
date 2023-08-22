def oselo(x,y,z):
    arr[x][y] = z
    if z == 1:
        a = 2
    else:
        a = 1
    for d in range(8):
        ni = x + di[d]
        nj = y + di[d]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == a:
            cnt = 0
            for n in range(1, N):
                cnt += 1
                ni = x + n * di[d]
                nj = y + n * di[d]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == z:
                    ni = x + di[d]
                    nj = y + di[d]
                    for j in range(cnt-1):
                        arr[ni][nj] = z
                        ni = ni + di[d]
                        nj = nj + di[d]






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
        oselo(x-1, y-1, z)
    print(arr)
