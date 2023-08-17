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


q = mycQueue(10)

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.enQueue(7)
q.enQueue(8)
q.enQueue(9)
q.enQueue(10)
q.enQueue(11)
q.enQueue(12)
q.enQueue(13)
q.enQueue(14)



