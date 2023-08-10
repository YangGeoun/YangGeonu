T = int(input())
for tc in range(1, 1+T):
    M = input()
    N = input()
    max_cnt = 0
    for i in range(len(M)):
        cnt = 0
        for j in range(len(N)):
            if N[j] == M[i]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')