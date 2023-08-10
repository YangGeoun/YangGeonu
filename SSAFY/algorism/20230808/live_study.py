def forBruteForce(N, M):
    for i in range(len(N)-len(M)+1):
        check = 1
        for j in range(len(M)):
            if N[i+j] != M[j]:
                check = 0
                break
        if check == 1:
            return i
    return -1


def whileBruteForce(N, M):
    i, j = 0, 0
    while j < len(M) and i < len(N):
        if N[i] != M[j]:
            i = i - j
            j = - 1
        i += 1
        j += 1
    if j == len(M):
        return i-len(M)
    else:
        return -1


def KMP(N, M, lst):
    i, j = 0, 0
    while j < len(M) and i < len(N):
        if N[i] != M[j]:
            j = lst[j]
        i += 1
        j += 1
    if j == len(M):
        return i - len(M)
    else:
        return -1


def BM(N, M):
    i = len(M) - 1
    j = len(M) - 1
    while 0 <= j < len(M) and i < len(N):
        if N[i] == M[j]:
            i -= 1
            j -= 1
        else:
            if N[i] in M:
                j = j - M.index(N[i]) + 1
            else:
                i += len(M)
                j += len(M)
    if j == 0:
        return i
    else:
        return -1



a = 'abcdabcdavdfeabcdabcef'
b = 'abcdabcef'
c = [0, 0, 0, 0, 0, 1, 2, 3, 0, 0]

a = list(a)
b = list(b)

print(forBruteForce(a, b))
print(whileBruteForce(a, b))
print(KMP(a, b, c))
print(BM(a, b))
