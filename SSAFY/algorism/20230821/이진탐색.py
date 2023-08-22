def inorder(n):
    global num_lst
    if n < N+1:   # 존재하는 정점이면
        inorder(n*2)
        num_lst.append(n)
        inorder(n*2+1)


T = int(input())
for tc in range(1,1+T):
    N = int(input())
    lst = [i for i in range(1+N)]
    num_lst = []
    inorder(1)
    ans1 = 0
    ans2 = 0
    for i in range(len(num_lst)):
        if num_lst[i] == N//2:
            ans1 = i+1

        if num_lst[i] == 1:
            ans2 = i+1

    print(f'#{tc}', ans2, ans1)