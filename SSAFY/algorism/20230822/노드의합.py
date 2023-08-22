T = int(input())
for tc in range(1, 1 + T):
    N, M, L = map(int, input().split())
    arr = [0 for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        arr[a] = b
    mid = N // 2
    while mid > 0:
        if mid*2+1 > N:
            arr[mid] = arr[mid*2]
        else:
            arr[mid] = arr[mid*2] + arr[mid*2+1]
        mid -= 1
    print(f'#{tc} {arr[L]}')