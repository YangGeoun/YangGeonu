T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()

    cnt = 0
    a = 0

    while a < len(A):
        cnt += 1
        for k in range(len(B)):
            if a + k < len(A):
                if A[a+k] == B[k]:
                    if k == len(B) - 1:
                        a += len(B)
                    continue
                else:
                    a += 1
                    break

    print(f'#{tc} {cnt}')