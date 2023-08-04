T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * 5002
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            arr[i] += 1
    P = int(input())
    station = []
    for _ in range(P):
        station.append(int(input()))
    ans = ''
    for el in station:
        ans += ' ' + str(arr[el])
    print(f'#{tc}{ans}')