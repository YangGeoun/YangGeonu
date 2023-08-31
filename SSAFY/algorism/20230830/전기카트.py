def solve(i, sum_v):
    global min_v
    if 0 not in visited:
        sum_v += arr[i][0]
        if min_v > sum_v:
            min_v = sum_v
        return

    else:
        for j in range(N):
            if j == i:
                continue
            if visited[j] == 0:
                visited[j] = 1
                solve(j, sum_v+arr[i][j])
                visited[j] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 999999
    visited = [0] * N
    visited[0] = 1
    solve(0,0)
    print(f'#{tc} {min_v}')