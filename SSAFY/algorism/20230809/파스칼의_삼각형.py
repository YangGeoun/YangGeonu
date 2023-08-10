def pas(num1, num2):
    if num1 == 1 or num2 == 1 or num1 == num2:
        return 1
    return pas(num1 - 1, num2 - 1) + pas(num1 - 1, num2)

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    i = 1
    j = 1

    print(f'#{tc}')
    if N == 1 :
        print(1,end='')
    while i < N:
        while j <= N:
            print(pas(i,j), end=' ')
            if i == N and j == N:
                break
            j += 1
            if i + 1 == j:
                i += 1
                j = 1
                print()
    print()