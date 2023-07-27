T = int(input())
cnt = 0

while T > 1:
    if T % 3 == 0:
        T /= 3
        cnt += 1
    elif T % 2 == 0:
        T /= 2
        cnt += 1
    else:
        T -= 1
        cnt += 1

print(cnt)