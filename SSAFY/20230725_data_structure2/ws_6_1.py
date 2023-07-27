# ws_6_1.py

# # 아래 함수를 수정하시오.
# def union_sets(set_a, set_b):
#     union_set = set_a.union(set_b)
#     return union_set


def union_sets(set_a, set_b):
    temp_list = list(set_a) + list(set_b)
    return set(temp_list)

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)