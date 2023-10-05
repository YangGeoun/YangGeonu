def solve(month, cost):
    global min_cost
    if month > 12:
        if min_cost > cost:
            min_cost = cost
        return
    if cost > min_cost:
        return
    solve(month+1, cost+arr[month-1]*d)
    solve(month+1, cost+m)
    solve(month+3, cost+m3)


T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    arr = list(map(int, input().split()))
    min_cost = y
    solve(1,0)
    print(f'#{tc} {min_cost}')