T = int(input())
for tc in range(1, 1+T):
    N, M = input().split()
    i, j = 0, 0
    cnt = 0
    while i < len(N) - len(M) + 1:
        for a in range(len(M)):
            if N[i+a] != M[a]:
                break
        else:
            i = i + len(M) - 1
            cnt += 1
        i += 1
    ans = len(N) - (len(M) - 1) * cnt
    print(f'#{tc} {ans}')