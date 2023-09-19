def solve(arr):
    if len(arr) < 2:
        return arr
    p = arr[-1]
    left = []
    right = []
    for i in range(len(arr)-1):
        if arr[i] >= p:
            right.append(arr[i])
        else:
            left.append(arr[i])
    left = solve(left)
    right = solve(right)
    return left + [p] + right


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {solve(arr)[N//2]}')