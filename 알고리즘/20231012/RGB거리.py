def solve(idx, sum_v, color):
    global min_v
    if sum_v >= min_v:
        return
    if idx == N:
        if min_v > sum_v:
            min_v = sum_v
        return
    for i in range(3):
        if i != color:
            solve(idx+1, sum_v + arr[idx][i], i)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 0xfffffff
solve(0, 0, -1)
print(min_v)