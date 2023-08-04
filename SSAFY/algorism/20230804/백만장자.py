T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    sum = 0
    while lst:
        max_index = 0
        max_v = 0
        for i in range(len(lst)):
            if max_v < lst[i]:
                max_v = lst[i]
                max_index = i
        for i in range(max_index):
            sum += max_v - lst[i]
        lst = lst[max_index+1:]
    print(f'#{tc} {sum})