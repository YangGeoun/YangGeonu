def inorder(n):
    if n < N+1:   # 존재하는 정점이면
        inorder(n*2)
        # ans.append(arr[n])
        print(arr[n], end='')
        inorder(n*2+1)


T = 10
for tc in range(1,1+T):
    N = int(input())
    arr = [0] * (N+1)
    for i in range(N):
        temp = list(input().split())
        arr[i+1] = temp[1]
    ans = []
    print(f"#{tc} ", end='')
    inorder(1)
    print()