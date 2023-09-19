def solve(index, x):
    global max_x
    if x < max_x:
        return
    if index == N:
        if max_x < x:
            max_x = x
        return
    for i in range(N):
        if i not in path:
            if arr[index][i] == 0:
                continue
            path[i] = i
            solve(index+1, x * arr[index][i] * 0.01)
            path[i] = -1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    max_x = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [-1] * N
    solve(0,1)
    a = "{:.6f}".format(max_x * 100)
    print(f'#{tc} {a}')
