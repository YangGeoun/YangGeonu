class mystack:
    def __init__(self, size):
        self.size = size
        self.s = [None] * size
        self.top = -1

    def pop(self):
        if self.top == -1:
            pass
        else:
            self.top -= 1
            return self.s[self.top+1]

    def push(self, item):
        if self.top == self.size:
            pass
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
            pass
        else:
            return self.s[self.top]

s = mystack(100)

for i in range(1, 11):
    N, input_str = input().split()
    for el in input_str:
        if s.is_empty():
            s.push(el)
        else:
            if s.peek() == el:
                s.pop()
            else:
                s.push(el)
    ans = ''
    while not s.is_empty():
        ans += s.pop() + ans

    print(ans)