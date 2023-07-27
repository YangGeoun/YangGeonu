import sys
def str_reverse(list1):
    temp_list = list(list1)
    temp_list.reverse()
    return ''.join(temp_list)

T = int(sys.stdin.readline())

for tc in range(T):
    str_in = sys.stdin.readline().split()
    for el in str_in:
        print(str_reverse(el),end=' ')
    print('')


