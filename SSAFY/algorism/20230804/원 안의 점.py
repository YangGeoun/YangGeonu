T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = 0
    for i in range(1, N+1):
        for j in range(N+1):
            if i**2 + j**2 <= N**2:
                num += 1
    num = num * 4
    num += 1
    print(f'#{tc} {num}')