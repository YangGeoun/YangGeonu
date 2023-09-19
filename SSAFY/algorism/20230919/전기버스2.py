def solve(index, cnt):
    global min_v
    if index >= N:
        if min_v > cnt:
            min_v = cnt
        return
    if min_v < cnt:
        return
    for i in range(index+1, index + tmp[index]+1):
        solve(i, cnt + 1)


T = int(input())
for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    min_v = 101
    solve(1,0)
    print(f'#{tc} {min_v-1}')