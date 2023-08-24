def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        if tree[n] == '+':
            return int(tree[ch1[n]]) + int(tree[ch2[n]])
        elif tree[n] == '-':
            return int(tree[ch1[n]]) - int(tree[ch2[n]])
        elif tree[n] == '*':
            return int(tree[ch1[n]]) * int(tree[ch2[n]])
        elif tree[n] == '/':
            return int(tree[ch1[n]]) // int(tree[ch2[n]])
        else:
            return n



for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for i in range(N):
        data = list(input().split())  # 문자열로받음
        idx = int(data[0])
        tree[idx] = data[1]  # 연산자일수도 있고 문자열 일수도
        if len(data) == 4:  # 좌우에 연결된 자식이 있다
            ch1[idx] = int(data[2])
            ch2[idx] = int(data[3])

      # 1번노드부터 시작해서 후위순회
    print(f'#{tc} {postorder(1)}')
    # print(ch1,ch2,tree)