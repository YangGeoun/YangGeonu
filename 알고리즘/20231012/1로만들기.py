def solve(N, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return
    if N == 1:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    if not N % 3:
        solve(N//3, cnt+1)
    if not N % 2:
        solve(N//2, cnt+1)
    solve(N-1, cnt+1)


num = int(input())
min_cnt = 0xffffff
solve(num, 0)
print(min_cnt)