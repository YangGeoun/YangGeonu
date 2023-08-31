def solve(cnt):
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            else:
                a[i], a[j] = a[j], a[i]
                if a not in lst[cnt]:
                    lst[cnt].append(a[:])
                a[i], a[j] = a[j], a[i]



T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    a = list(a)
    b = int(b)
    ans = []
    lst = [[] for _ in range(b)]
    solve(0)
    count = 1
    while count < b:
        for el in lst[count]:
            a = el
            solve(count + 1)
        count += 1

    for el in lst[b-1]:
        ans.append(int(''.join(el)))

    print(ans)