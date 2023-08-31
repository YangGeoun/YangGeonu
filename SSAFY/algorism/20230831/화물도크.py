T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    lst.sort(key=lambda x: x[1])
    lst = [[0,0]] + lst
    cnt = 0
    j = 0
    for i in range(1, N+1):
        if lst[i][0] >= lst[j][1]:
            cnt += 1
            j = i
    print(f'#{tc} {cnt}')