T = int(input())
di1 = [-1,1,0,0,-1,-1]
dj1 = [0,0,-1,1,-1,1]
di2 = [-1,1,0,0,1,1]
dj2 = [0,0,-1,1,-1,1]


for tc in range(1, T+1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            tmp_lst = [(i,j)]
            while len(tmp_lst) < 4:
                max_v = 0
                max_idx = (0, 0)
                for el in tmp_lst:
                    x, y = el
                    for d in range(6):
                        if y % 2:
                            ni = x + di2[d]
                            nj = y + dj2[d]
                            if 0 <= ni < H and 0 <= nj < H and (ni, nj) not in tmp_lst:
                                if max_v < arr[ni][nj]:
                                    max_v = arr[ni][nj]
                                    max_idx = (ni, nj)
                tmp_lst.append(max_idx)
            sum_v = 0
            for x,y in tmp_lst:
                sum_v += arr[x][y]
            if ans < sum_v:
                ans = sum_v
    print(ans)



