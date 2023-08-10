T = int(input())
for tc in range(1, 1+T):
    input_str = input()
    ans = 1
    n = len(input_str)
    for i in range(n//2):
        if input_str[i] != input_str[n - i - 1]:
            ans = 0
    print(f'#{tc} {ans}')