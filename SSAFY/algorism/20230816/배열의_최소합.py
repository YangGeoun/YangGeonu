def minsum(i,N,s):
    global min
    if i == N:
        sum = 0
        for k in range(N):
            sum += arr[k][a[k]-1]
        if min > sum:
            min = sum
    else:
        for j in range(i,N):
            a[i], a[j] = a[j], a[i]
            minsum(i+1,N)
            a[i], a[j] = a[j], a[i]


T = int(input())
for tc in range(1, T + 1):
    min = 100
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = [i + 1 for i in range(N)]
    b = [0] * N
    minsum(0,N)
    print(f'#{tc} {min}')