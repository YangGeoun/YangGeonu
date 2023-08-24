T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    lst = list(input().split())
    ans = []
    if N % 2 == 0:
        for i in range(N//2):
            ans.append(lst[i])
            ans.append(lst[N//2 + i])
    else:
        for i in range(N//2):
            ans.append(lst[i])
            ans.append(lst[N//2 + i + 1])
        ans.append(lst[N//2])

    print(f'#{tc}', *ans)