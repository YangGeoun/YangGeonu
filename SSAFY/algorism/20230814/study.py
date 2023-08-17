# 중위표기법 -> 후위표기법

exp = '6+5*(2-8)/2'
post_exp = ''
stack = []

isp = {'*': 2,'/': 2,'+': 1,'-': 1,'(': 0}
icp = {'*': 2,'/': 2,'+': 1,'-': 1,'(': 3}

for c in exp:
    if c in '+-*/()':
        if not stack:
            stack.append(c)
        elif isp[stack[-1]] > icp[c]:
            post_exp += stack
    else:
        post_exp += c


