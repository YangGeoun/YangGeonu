T = int(input())
for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    max_len = 0
    for el in arr:
        if max_len < len(el):
            max_len = len(el)
    for i in range(len(arr)):
        while len(arr[i]) != max_len:
            arr[i] += '*'
    ans = ''
    for j in range(max_len):
        for i in range(5):
            if arr[i][j] != '*':
                ans += arr[i][j]
    print(f'#{tc} {ans}')