T = int(input())

di = [1,-1,0,0]
dj = [0,0,1,-1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j
                break
    q = [(si,sj)]
    visited[si][sj] = 1
    ans = 2
    while q:
        x, y = q.pop(0)
        if arr[x][y] == 3:
            ans = visited[x][y]
            break
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[x][y] + 1
                    q.append((ni, nj))

    print(f'#{tc}', ans-2)

