def solution(s):
    lst = list(s.split())
    stack = []
    for el in lst:
        if el != 'Z':
            stack.append(el)
        else:
            stack.pop()

    answer = 0
    for el in stack:
        answer += el

    return answer
