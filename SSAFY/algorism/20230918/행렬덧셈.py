
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    max_sum = 0
    min_sum = 1000000

    for i in range(N - M + 1):
        sum = 0
        for j in range(M):
            sum += lst[i + j]
        if max_sum < sum:
            max_sum = sum
        if min_sum > sum:
            min_sum = sum

    print(f'#{tc} {max_sum - min_sum}')