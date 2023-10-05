def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        p[y] = x
    else:
        p[x] = y


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    p = [x for x in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        if find_set(a) != find_set(b):
            union(a, b)
    ans = []

    cnt = 0
    # 1번부터 N번까지의 사람
    for i in range(1, N + 1):
        if i == p[i]:
            cnt += 1

    print(f'#{tc}', cnt)