T = int(input())

for tc in range(1, T+ 1):
    N, Q = map(int, input().split())
    box_lst = [0] * N
    for a in range(1, Q+1):
        i, j = map(int, input().split())
        for index in range(i-1, j):
            box_lst[index] = a
    print(f'#{tc}', end=' ')
    print(*box_lst, end=' ')
    print()
