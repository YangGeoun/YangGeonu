class myQueue:
    def __init__(self, size):
        self.size = size
        self.q = [0] * size
        self.front = -1
        self.rear = -1

    def enQueue(self,item):
        if self.isFull():
            print('큐가 가득찼습니다.')
            return
        self.rear += 1
        self.q[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print('큐가 비어있습니다.')
        self.front += 1
        return self.q[self.front]

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def Qpeek(self):
        return self.q[self.rear]

    def isFull(self):
        if self.rear == self.size - 1:
            return True
        return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = myQueue(1001)
    for el in arr:
        q.enQueue(el)
    for i in range(M):
        q.deQueue()
        q.enQueue(arr[i % N])
    print(f'#{tc} {q.deQueue()}')
