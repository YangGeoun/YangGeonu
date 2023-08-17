T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    stack = []
    x1 = 0
    y1 = 0
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    ans = 0
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x1 = i
                y1 = j

    stack = [(x1, y1)]
    while stack:
        x, y = stack[-1]
        if arr[x][y] == 3:
            ans = 1
            break
        visited[x][y] = 1
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if (arr[ni][nj] == 0 or arr[ni][nj] == 3) and visited[ni][nj] == 0:
                    stack.append((ni, nj))
                    break
        else:
            stack.pop()

    print(f'#{tc} {ans}')
