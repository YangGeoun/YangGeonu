def change(r, c, s):
    for i in range(8):
        temp = []
        for j in range(1, N):
            ni, nj = r + di[i] * j, c + dj[i] * j
            if 0 <= ni < N and 0 <= nj < N:
                if not arr[ni][nj]:
                    break
                elif arr[ni][nj] != s:
                    temp.append((ni, nj))
                elif arr[ni][nj] == s:
                    for ti, tj in temp:
                        arr[ti][tj] = s
                    break
                else:
                    temp = []
            else:
                temp = []


T = int(input())
di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, -1, 1, -1, 1]
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = 2

    for i in range(M):
        x, y, z = map(int, input().split())
        arr[x - 1][y - 1] = z
        change(x - 1, y - 1, z)

    b = 0
    w = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                b += 1
            elif arr[i][j] == 2:
                w += 1

    print(f'#{tc} {b} {w}')