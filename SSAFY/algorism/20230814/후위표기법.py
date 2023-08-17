# 중위 표기법 -> 후위 표기법
# 연산 우선순위가 높은 애가 먼저 출력될 수 있도록 해야 한다.

# 우선 순위를 비교하기 위한 딕셔너리 생성
# 괄호 때문에 우선순위표를 2개 만들어 줄것이다
# 괄호는 stack안에 있을때랑 밖에 있을때 우선 순위가 다르다.
# 스택안에서는 괄호안에 다른 연산자들 다 처리하고 괄호가 없어져야 하니까 우선순위가 낮음
# 스택밖에서는 스택에 들어갈때는 다른 연산자들보다 관호가 먼저 처리되어야 해서 우선순위가 높다.
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}

stack = []
exp = '6+5*(2-8)/2'
post_exp = ''
for c in exp:
    # 하나씩 읽어오기
    # 피연산자 vs 연산자
    # 피연산자면 출렫
    # 연산자라면 우선순위에 따라 스택에 넣거나 출력
    if c in '+-*/()':   # 연산자
        if c == ')':
            while stack[-1] != '(':
                post_exp += stack.pop()
            stack.pop()
            continue                                       # 다음 토큰 읽어오기
        if not stack:
            stack.append(c)
        # stack[top]의 연산자보다 우선순위가 높으면 그냥 넣기
        elif isp[stack[-1]] < icp[c]:                       # 넣는애의 우선 순위가 top의 우선 순위보다 더 높으면
            stack.append(c)                                 # 바로 push
        else:
            while stack and isp[stack[-1]] >= icp[c]:        # 넣는애보다 우선순위가 낮은애가 나올때까지
                post_exp += stack.pop()                      # 넣는애보다 우선순위가 높거나 같으면 계속해서
            stack.append(c)
    else:                                                    # pop 해준다.
        post_exp += c

while stack:
    post_exp += stack.pop()                      # 스택에 남아있는 연산자 출력

print(post_exp)


