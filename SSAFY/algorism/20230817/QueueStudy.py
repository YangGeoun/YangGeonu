class myQueue:
    def __init__(self, size):
        self.size = size
        self.q = [0] * size
        self.front = -1
        self.rear = -1

    def enQueue(self,item):
        if self.isFull():
            print('큐가 가득찼습니다.')
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


q = myQueue(100)

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
q.enQueue(6)
q.enQueue(7)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())



