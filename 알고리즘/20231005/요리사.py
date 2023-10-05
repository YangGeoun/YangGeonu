def subset(idx,cnt):
    global min_v
    if cnt == N//2:
        a_lst = []
        b_lst = []
        sum1 = 0
        sum2 = 0
        for i in range(N):
            if tmp[i]:
                a_lst.append(i)
            else:
                b_lst.append(i)
        for i in range(N//2):
            for j in range(i+1,N//2):
                sum1 += arr[a_lst[i]][a_lst[j]]
                sum1 += arr[a_lst[j]][a_lst[i]]
                sum2 += arr[b_lst[i]][b_lst[j]]
                sum2 += arr[b_lst[j]][b_lst[i]]
        dif = abs(sum1 - sum2)
        if min_v > dif:
            min_v = dif
        return
    if idx == N:
        return
    tmp[idx] = 1
    subset(idx+1, cnt+1)
    tmp[idx] = 0
    subset(idx+1, cnt)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    tmp = [0] * N
    min_v = 0xfffffff

    subset(0,0)
    print(f'#{tc} {min_v}')