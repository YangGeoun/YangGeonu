N, M = map(int, input().split())

list_a = []
list_b = []
list_s = [0] * M
list_sum = []

for i in range(N):
    list_sum.append(list_s[:])

for i in range(N):
    temp = list(map(int, input().split()))
    list_a.append(temp)
for i in range(N):
    temp = list(map(int, input().split()))
    list_b.append(temp)

for i in range(N):
    for j in range(M):
        list_sum[i][j] = list_a[i][j] + list_b[i][j]
        
for i in range(N):
    for j in range(M):
        print(list_sum[i][j],end=' ')
    print('')