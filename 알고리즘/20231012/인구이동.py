def find_set(x):
    if p[x] == x:
        return x

    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    # 1. 이미 같은 집합인지 확인
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 이미 같은 집합이다.
    if x == y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 설정
    if x < y:
        p[y] = x
    else:
        p[x] = y
    return


N, L, R = map(int, input().split())
p = [i for i in range(1, N**2)]
