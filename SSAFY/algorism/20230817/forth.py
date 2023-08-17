T = int(input())
for tc in range(1, T + 1):
    susik = input().split()
    stack = []
    ans = 0

    for i in susik:
        if i not in '+*./-':  # 피연산자면
            stack.append(int(i))
        else:
            if i == '+':
                if len(stack) < 2:
                    ans = 'error'
                    break
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 + op1)
            elif i == '*':
                if len(stack) < 2:
                    ans = 'error'
                    break
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 * op1)
            elif i == '-':
                if len(stack) < 2:
                    ans = 'error'
                    break
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif i == '/':
                if len(stack) < 2:
                    ans = 'error'
                    break
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 // op1)
            elif i == '.':
                if len(stack) == 1:
                    ans = stack[0]
                else:
                    ans = 'error'
                    break

    print(f'#{tc}', ans)