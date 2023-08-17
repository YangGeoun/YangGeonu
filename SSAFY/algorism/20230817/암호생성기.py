

T = 10
for tc in range(1, T + 1):
    t = int(input())
    q = list(map(int, input().split()))
    i = 1
    while q[-1] != 0:
        temp = q.pop(0)
        temp -= i
        if temp < 1:
            temp = 0
        q.append(temp)
        i = (i + 1) % 6
        if i == 0:
            i += 1
    print(f'#{tc}',end=' ')
    print(*q)
