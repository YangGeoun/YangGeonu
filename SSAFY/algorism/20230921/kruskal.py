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


V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
edge.sort(key=lambda x: x[2])

# 사이클 발생 여부를 union find 로 해결
parent = [i for i in range(V)]

cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        if cnt == V:
            break

print(sum_weight)