T = 10
for tc in range(1,T+1):
    N = int(input())
    exp = input()
    stack = []
    post_exp = ''
    for el in exp:
        if el not in '+*':
            post_exp += el
        else:
            if not stack:
                stack.append(el)
            else:
                if el == '+':
                    while stack:
                        post_exp += stack.pop()
                    stack.append(el)
                else:
                    if stack[-1] == '*':
                        post_exp += stack.pop()
                        stack.append(el)
                    else:
                        stack.append(el)

    while stack:
        post_exp += stack.pop()

    for el in post_exp:
        if el not in '+*':
            stack.append(int(el))
        else:
            if el == '+':
                stack.append(stack.pop()+stack.pop())
            else:
                stack.append(stack.pop()*stack.pop())

    print(f'#{tc} {stack[-1]}')