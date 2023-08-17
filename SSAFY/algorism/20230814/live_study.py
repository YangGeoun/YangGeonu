stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

susik = ''
top = -1

for el in susik:
    if el not in '(+-*/)':
        susik += el
    elif el == ')':
        while stack[top] != '(':
            susik += stack[top]
            top -= 1
        top -= 1
    else:
        if top == -1 or icp[stack[top]] < icp[el]:
            top += 1
            stack[top] = el
        elif isp[stack[top]] >= icp[el]:
            while top > -1 and isp[stack[top]] >= icp[top]:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = el
print(stack)