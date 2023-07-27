import sys
T = int(sys.stdin.readline())
stack_list = []

for tc in range(T):
    A = sys.stdin.readline().split()
    if A[0] == 'push':
        stack_list.append(A[1])
    elif A[0] == 'pop':
        if len(stack_list):
            print(stack_list.pop())
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(stack_list))
    elif A[0] == 'empty':
        if len(stack_list):
            print(0)
        else:
            print(1)
    elif A[0] == 'top':
        if len(stack_list):
            print(stack_list[-1])
        else:
            print(-1)