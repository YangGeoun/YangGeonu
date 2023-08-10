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
        if self.top == self.size - 1:
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
            return False
        return self.s[self.top]


T = int(input())
for tc in range(1, T+1):
    input_str = input()
    stack1 = mystack(1000)
    for el in input_str:
        if stack1.is_empty():
            stack1.push(el)
        else:
            if stack1.peek() == el:
                stack1.pop()
            else:
                stack1.push(el)
    ans = stack1.top + 1
    print(f'#{tc} {ans}')