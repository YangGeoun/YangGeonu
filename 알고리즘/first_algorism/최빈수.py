T = int(input())

for n in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max_count = 1
    count = 1
    index = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i + 1]:
            count += 1
            if count >= max_count:
                max_count = count
                index = i
        else:
            count = 1
    print(f'#{N} {arr[index]}')
