heap = [None] * 100
heap_pointer = 1


def heap_push(data):
    global heap_pointer
    heap[heap_pointer] = data
    current = heap_pointer
    parent = current // 2
    while current != 1 and heap[parent] < heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2
    heap_pointer += 1


def heap_pop():
    global heap_pointer
    result = heap[1]
    if heap_pointer == 1:
        return None
    heap_pointer -= 1
    heap[1] = heap[heap_pointer]
    parent = 1
    child = parent * 2
    if child + 1 <= heap_pointer:
        if heap[child] < heap[child+1]:
            child += 1

    while child <= heap_pointer and heap[child] > heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = parent * 2
        if child + 1 <= heap_pointer:
            if heap[child] < heap[child+1]:
                child += 1
    return result


for i in range(1, 21):
    heap_push(i)
print(heap)