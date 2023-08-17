for tc in range(1, 11):
    N = int(input())
    input_str = input()
    stack = []
    after_str = ''
    for el in input_str:
        if el == '+':
            if not stack:
                stack.append(el)
            else:
                after_str += stack.pop()
                stack.append(el)
        else:
            after_str += el
    while stack:
        after_str += stack.pop()
    print(after_str)
    #
    # for el in after_str:
    #     if el != '+':
    #         stack.append(el)
    #     else:
    #         op2 = int(stack.pop())
    #         op1 = int(stack.pop())
    #         stack.append(op2+op1)

    # print(f'#{tc} {stack[0]}')