S = int(input())
E = int(input())

arr = [0,0] +[1 for i in range(E-1)]

for i in range(2, E//2):
    num = i
    while num + i <= E:
        num += i
        arr[num] = 0

sum = 0
min = 0
for i in range(E,S-1,-1):
    if arr[i] == 1:
        sum += i
        min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)