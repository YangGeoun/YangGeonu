T = int(input())
for tc in range(1,1+T):
    N = int(input())
    cost_lst = list(map(int, input().split()))
    ans = 0
    start = 0
    end = len(cost_lst) - 1
    while start < end:
        max_v = cost_lst[start]
        max_i = start
        for j in range(start, len(cost_lst)):
            if max_v < cost_lst[j]:
                max_v = cost_lst[j]
                max_i = j
        for k in range(max_i-start):
            ans += max_v - cost_lst[k + start]
        start = max_i + 1
    print(f'#{tc} {ans}')


