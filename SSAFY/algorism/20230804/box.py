T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    max_cnt = 0
    for j in range(10):
        cnt = 0
        for i in range(j+1,10):
            if lst[j] > lst[i]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(max_cnt)