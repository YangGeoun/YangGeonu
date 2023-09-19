def solve(index, sum_v):
    global max_v, ans
    if ans <= sum_v:
        return
    if index == N:
        if B <= sum_v:
            if ans > sum_v:
                ans = sum_v
        return
    path[index] = arr[index]
    solve(index + 1, sum_v + arr[index])
    path[index] = 0
    solve(index + 1, sum_v)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = 0
    ans = 10000000
    path = [0] * N
    solve(0, 0)
    print(f'#{tc} {ans-B}')