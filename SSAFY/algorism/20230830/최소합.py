def solve(x, y, now_sum):
    global min_v
    now_sum += arr[x][y]
    if x == N-1 and y == N -1:
        if min_v > now_sum:
            min_v = now_sum
        return
    else:
        if x < N-1:
            solve(x+1, y,now_sum)
        if y < N-1:
            solve(x, y+1,now_sum)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 999999
    solve(0, 0, 0)
    print(f'#{tc} {min_v}')
