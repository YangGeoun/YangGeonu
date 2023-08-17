def solve(start, end):
    if start == end:
        return start

    mid = (end + start) // 2
    w1 = solve(start, mid)
    w2 = solve(mid+1, end)
    if

    return solve(solve(start,mid), solve(mid+1,end))


T = int(input())
for tc in range(1,T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'!{tc} {solve(0,N-1)+1}')

