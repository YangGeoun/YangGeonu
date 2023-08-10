class mystack:
    def __init__(self, size):
        self.size = size
        self.s = [None] * size
        self.top = -1

    def pop(self):
        if self.top == -1:
            print('underflow')
        else:
            self.top -= 1
            return self.s[self.top+1]

    def push(self, item):
        if self.top == 9:
            print('overflow')
        else:
            self.top += 1
            self.s[self.top] = item

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        if self.top == -1:
            print('Empty')
        else:
            print(self.s[self.top])


stack1 = mystack(10)

stack1.push(1)
stack1.push(2)
stack1.push(3)

print(stack1.pop())
print(stack1.pop())
print(stack1.pop())

print(stack1.is_empty())
