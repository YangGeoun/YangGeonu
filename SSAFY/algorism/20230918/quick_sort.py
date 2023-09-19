import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = arr.pop()
    left = [e for e in arr if e < mid]
    right = [e for e in arr if e >= mid]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [mid] + right


def quick_sort2(arr,l,r):
    if l >= r:
        return
    p = partition1(arr, l, r)  # 피벗 위치

    quick_sort2(arr, l, p-1)
    quick_sort2(arr, p+1, r)


# hoare  l,r기준, pivot 잡고, 작은값 큰값 나누기   피벗 위피 반환
def partition1(arr, l, r):
    i = l
    j = r
    pivot = arr[l]
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]

    return j


def partition2(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l,r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


# [89, 15, 25, 44, 66, 28, 37, 94, 83, 19]
lst = []
for i in range(10):
    lst.append(random.randint(1,100))
print(lst)
quick_sort2(lst,0,len(lst)-1)
print(lst)