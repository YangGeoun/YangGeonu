T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stairs = []
    people = []
    for i in range(N):
        for j in range(N):
            tmp = arr[i][j]
            if tmp == 0:
                continue
            elif tmp == 1:
                people.append((i, j))
            else:
                stairs.append((tmp, i, j))
    for person in people:
        pi, pj = person
        min_h = 11
        for stair in stairs:
            height, si, sj = stair


