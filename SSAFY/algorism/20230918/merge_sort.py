import random


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    arr1 = merge_sort(arr[:len(arr)//2])
    arr2 = merge_sort(arr[len(arr)//2:])
    new_arr = []

    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
    new_arr += arr1 + arr2

    return new_arr


def merge_sort2(arr, s, e):
    if s == e:
        return
    # s = 0
    # e = len(arr)-1
    mid = (s + e) // 2
    merge_sort2(arr,s,mid)
    merge_sort2(arr,mid+1,e)
    i = s
    j = mid + 1
    tmp = []
    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= mid:
        tmp.append(arr[i])
        i += 1
    while j <= e:
        tmp.append(arr[j])
        j += 1

    j = 0
    for i in range(s,e+1):
        arr[i] = tmp[j]
        j +=1


lst = []
for i in range(30):
    lst.append(random.randint(1,100))
print(lst)
merge_sort2(lst,0,29)
print(lst)