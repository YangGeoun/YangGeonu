def solve(cnt, sum_v):
    global min_v
    if cnt == N:
        if min_v > sum_v:
            min_v = sum_v
        return
    if sum_v > min_v:
        return
    for i in range(N):
        if i not in path:
            path.append(i)
            solve(cnt+1, sum_v + arr[cnt][i])
            path.remove(i)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    min_v = 20000
    path = []
    solve(0, 0)
    print(f'#{tc} {min_v}')