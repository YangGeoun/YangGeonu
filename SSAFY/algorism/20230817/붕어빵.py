T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    count = [0] * 11112
    for el in arr:
        count[el] += 1
    num_bung = [0] * 11112
    for i in range(M,len(num_bung),M):
        num_bung[i] = K
    for i in range(len(num_bung)-1):
        num_bung[i+1] += num_bung[i]
    for i in range(len(count)-1):
        count[i+1] += count[i]

    if N < len(arr):
        ans = 'Impossible'
    else:
        for i in range(len(count)):
            if count[i] > num_bung[i]:
                ans = 'Impossible'
                break
        else:
            ans = 'Possible'

    print(f'#{tc} {ans}')