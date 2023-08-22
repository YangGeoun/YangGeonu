def heq():
    global last
    tmp = heap[1]             # 루트 백업
    heap[1] = heap[last]      # 삭제할 노드의 키를 루트에 저장
    last -= 1                 # 마지막 노드 삭제
    p = 1                     # 루트에 옮긴 값을 자식과 비교
    c = p * 2                 # 왼쪽 자식(비교할 자식노드 번호)
    while c <= last:
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


heap = []
