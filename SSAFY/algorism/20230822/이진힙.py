T = int(input())
for tc in range(1,1+T):
    N = int(input())
    inp_lst = list(map(int, input().split()))
    heap = [0]
    last = 0
    for el in inp_lst:
        heap.append(el)
        last += 1
        ic_index = last
        while ic_index > 1 and heap[ic_index // 2] > heap[ic_index]:
            heap[ic_index // 2], heap[ic_index] = heap[ic_index], heap[ic_index // 2]
            ic_index = ic_index // 2
    n = last // 2
    ans = 0
    while n > 0:
        ans += heap[n]
        n = n // 2

    print(f'#{tc} {ans}')