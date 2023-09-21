import math


def find_set(x):
    if parent[x] == x:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]


def union(x,y):
    # 1. 이미 같은 집합인지 확인
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 이미 같은 집합이다.
    if x == y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 설정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    islands = list(zip(x,y))
    lst = []
    for i in range(N):
        for j in range(i+1, N):
            dist = math.sqrt(abs(islands[i][0] - islands[j][0])**2 + abs(islands[i][1] - islands[j][1])**2)
            lst.append((dist, i, j))
    lst.sort()
    parent = [x for x in range(N)]

    cnt = 0
    ans_lst = []
    for dist, s, e in lst:
        # 싸이클이 발생하지 않는다면
        if find_set(s) != find_set(e):
            cnt += 1
            ans_lst.append(dist)
            union(s, e)
            if cnt == N:
                break
    ans = 0
    for el in ans_lst:
        ans += el**2

    print(f'#{tc}', round(ans*E))