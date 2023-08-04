for _ in range(1, 11):
    tc = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    di = [0, 0, -1]
    dj = [1, -1, 0]
    #   0오  1왼  2위
    j = ladder[99].index(2)
    i = 99
    d = 2
    while i > 0:
        if d == 2:
            if ladder[i][j+1] == 1:
                d = 0
            if ladder[i][j-1] == 1:
                d = 1
        else:
            if ladder[i-1][j] == 1:
                d = 2
        i = i + di[d]
        j = j + dj[d]

    print(j)