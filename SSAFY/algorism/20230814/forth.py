T = int(input())
for tc in range(1, T+1):
    input_str = input().split()
    stack = []
    ans = 0
    for el in input_str:
        if el == '+':
            if len(stack) < 2:
                ans = 'error'
                break
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 + op2)
        elif el == '-':
            if len(stack) < 2:
                ans = 'error'
                break
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 - op2)
        elif el == '*':
            if len(stack) < 2:
                ans = 'error'
                break
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 * op2)
        elif el == '/':
            if len(stack) < 2:
                ans = 'error'
                break
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(op1 // op2)
        elif el == '.':
            if len(stack) == 1:
                ans = stack[0]
            else:
                ans = 'error'
                break
        else:
            stack.append(el)

    print(f'#{tc} {ans}')