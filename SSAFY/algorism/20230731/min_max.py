T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = 1000000
    max_num = 1
    for el in arr:
        if el < min_num:
            min_num = el
        if el > max_num:
            max_num = el
    print(f'#{tc} {max_num-min_num}')

