# ws_6_5.py

# # 아래 함수를 수정하시오.
# def difference_sets(set_a, set_b):
#     return set_a.difference(set_b)


def difference_sets(set_a, set_b):
    temp_list = list(set_a)
    for el in set_a:
        if el in set_b:
            temp_list.remove(el)
    return set(temp_list)


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)