def heap_push():
    global heap_pointer
    child = heap_pointer
    parent = child//2
    while heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent
        parent = child // 2


heap = [0] * 100
heap_pointer = 1