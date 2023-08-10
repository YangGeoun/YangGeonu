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
            print(self.s[self.top])


T = int(input())
for tc in range(1, T+1):
    input_str = input()
    stack1 = mystack(1000)
    check = 1
    i = 0

    while i < len(input_str):
        if input_str[i] == '\\':
            i += 1
        if input_str[i] == '[' or input_str[i] == '{' or input_str[i] == '(':
            stack1.push(input_str[i])
        if input_str[i] == ']':
            if stack1.is_empty():
                check = 0
                break
            if stack1.pop() != '[':
                check = 0
                break
        if input_str[i] == '}':
            if stack1.is_empty():
                check = 0
                break
            if stack1.pop() != '{':
                check = 0
                break
        if input_str[i] == ')':
            if stack1.is_empty():
                check = 0
                break
            if stack1.pop() != '(':
                check = 0
                break
        i += 1

    if not stack1.is_empty():
        check = 0

    print(f'#{tc} {check}')
