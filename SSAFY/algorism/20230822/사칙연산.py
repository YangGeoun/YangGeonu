def postorder(n):
    if n:   # 존재하는 정점이면
        postorder(ch1[n])
        postorder(ch2[n])
        # print(out_lst[n-1], end = '')
        ans.append(out_lst[n-1])

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
    ans = []
    postorder(1)
    stack = []
    for el in ans:
        if el == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif el == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif el == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif el == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b//a)
        else:
            stack.append(int(el))
    print(f'#{tc} {stack[0]}')