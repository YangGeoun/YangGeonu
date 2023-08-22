T = int(input())
for tc in range(1,1+T):
    lst = list(map(int, input()))
    cnt = lst[0]
    state = lst[0]
    for el in lst:
        if el != state:
            cnt += 1
            state = el
    print(f'#{tc} {cnt}')
