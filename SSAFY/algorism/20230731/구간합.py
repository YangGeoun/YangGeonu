T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_sum = 0
    min_sum = 1000000
    for i in range(len(num_list) - M + 1):
        sum = 0
        for j in range(M):
            sum += num_list[i+j]
        if max_sum < sum:
            max_sum = sum
        if min_sum > sum:
            min_sum = sum

    print(f'#{tc} {max_sum-min_sum}')

