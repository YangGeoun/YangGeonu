
T = int(input())

for N in range(T):
    n = int(input())

    arr = []
    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
    

    print(f'#{N+1}')
    for i in range(n):
        for j in range(n):
            print(arr[n-1-j][i], end='')
        print(' ', end='')    
        for j in range(n):    
            print(arr[n-1-i][n-1-j], end='')
        print(' ', end='')    
        for j in range(n):
            print(arr[j][n-1-i], end='')   
        print(' ', end='')    
        print('')