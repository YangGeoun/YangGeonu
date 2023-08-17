class mycQueue:
    def __init__(self, size):
        self.size = size
        self.q = [0] * size
        self.front = 0
        self.rear = 0

    def enQueue(self, item):
        if self.isFull():
            print( '큐가 가득찼습니다.')
        else:
            self.q[self.rear] = item
            self.rear = (self.rear + 1) % (self.size)

    def deQueue(self):
        if self.isEmpty():
            return '큐가 비어있습니다.'
        self.front = (self.front + 1) % (self.size)
        return self.q[self.front - 1]

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def Qpeek(self):
        return self.q[self.rear]

    def isFull(self):
        if (self.rear + 1) % (self.size) == self.front:
            return True
        return False


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = mycQueue(1001)
    for el in arr:
        q.enQueue(el)
    for i in range(M):
        q.deQueue()
        q.enQueue(arr[i % N])
    print(f'#{tc} {q.deQueue()}')
