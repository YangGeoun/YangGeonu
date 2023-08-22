def inorder(n):
    if n:   # 존재하는 정점이면
        inorder(ch1[n])
        print(out_lst[n-1], end = '')
        inorder(ch2[n])


T = 10
for tc in range(1,T+1):
    N = int(input())
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    out_lst = []
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
    print(f'#{tc}', end=' ')
    inorder(1)
    print()