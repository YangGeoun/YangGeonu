def solve(start, end):
    if start == end:
        return start

    mid = (end + start) // 2
    w1 = solve(start, mid)
    w2 = solve(mid+1, end)

    if arr[w1] > arr[w2]:
        if arr[w1] == 3 and arr[w2] == 1:
            return w2
        else:
            return w1
    elif arr[w1] < arr[w2]:
        if arr[w1] == 1 and arr[w2] == 3:
            return w1
        else:
            return w2
    else:
        return w1


T = int(input())
for tc in range(1,T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'!{tc} {solve(0,N-1)+1}')

