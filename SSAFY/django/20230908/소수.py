S = int(input())
E = int(input())

sum = 0
min = 0
for i in range(E, S-1, -1):
    cnt = 0
    for j in range(1,i):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        sum += i
        min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
