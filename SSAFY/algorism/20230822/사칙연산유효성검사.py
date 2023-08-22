T = 10
for tc in range(1,T+1):
    N = int(input())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    out_lst = []
    ans = 1
    for i in range(N):
        inp = list(input().split())
        if len(inp) == 4:
            a,b,c,d = inp
            ch1[int(a)] = int(c)
            ch2[int(a)] = int(d)
            out_lst.append(b)
        elif len(inp) == 3:
            a,b,c = inp
            out_lst.append(b)
            ch1[int(a)] = int(c)
        else:
            a,b = inp
            out_lst.append(b)
    for i in range(len(out_lst)):
        if out_lst[i].isdigit():
            if ch1[i+1] != 0:
                ans = 0
        else:
            if ch2[i+1] == 0:
                ans = 0
    print(f'#{tc} {ans}')