import random


def s_sort(i, N, arr):
    if i == N-1:
        return arr
    else:
        min_v = 100
        min_idx = 0
        for j in range(i, N):
            if min_v > arr[j]:
                min_v = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return s_sort(i+1,N,arr)


N = int(input())
lst = [random.randint(1,100) for _ in range(N)]
print(s_sort(0,N,lst))
