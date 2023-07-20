def times(x, y, n):
    result = []
    for i in range(n):
        result.append(x[i]*y[i])
    return result


def sum(x):
    s = 0
    for i in x:
        s += i
    return s



T = int(input())


for N in range(T):
    maxSum = 0
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if n > m:
        for i in range(n-m+1):
            temp = []
            for j in range(m):
                temp.append(x[i+j])
            if maxSum < sum(times(temp, y, m)):
                maxSum = sum(times(temp, y, m))
    elif n < m:
        for i in range(m-n+1):
            temp = []
            for j in range(n):
                temp.append(y[i+j])
            if maxSum < sum(times(temp, x, n)):
                maxSum = sum(times(temp, x, n))
    print(f'#{N+1} {maxSum}')


