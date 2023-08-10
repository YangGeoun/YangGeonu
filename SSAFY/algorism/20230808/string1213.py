def matchCnt(N, M):
    cnt = 0
    for i in range(len(N)-len(M)+1):
        check = 1
        for j in range(len(M)):
            if N[i+j] != M[j]:
                check = 0
                break
        if check == 1:
            cnt += 1
    return cnt


for tc in range(1, 11):
    T = int(input())
    M = input()
    N = input()
    print(f'#{tc} {matchCnt(N, M)}')