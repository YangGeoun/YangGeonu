T = int(input())
for tc in range(1, 1 + T):
    temp = input().strip('#')
    t, N = map(int, temp.split())
    arr = list(input().split())
    num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    num_lst = [0] * 10

    for el in arr:
        num_lst[num_dict[el]] += 1

    for i in range(len(num_lst) - 1):
        num_lst[i + 1] += num_lst[i]

    ans = [0] * N
    for el in arr:
        num_lst[num_dict[el]] -= 1
        ans[num_lst[num_dict[el]]] = el

    result = ' '.join(ans)

    print(f'#{tc}')
    print(result)