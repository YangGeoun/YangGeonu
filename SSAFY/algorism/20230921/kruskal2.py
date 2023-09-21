def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        p[y] = p[x]
    else:
        p[x] = p[y]


V, E = map(int, input().split())
graph = []
for _ in range(E):
    graph.append(tuple(map(int,input().split())))
graph.sort(key=lambda x: x[2])
p = [x for x in range(V)]
MST = []
while len(MST) < V-1:
    s, e, w = graph.pop(0)
    if find_set(s) != find_set(e):
        MST.append((s, e, w))
        union(s, e)
print(MST)