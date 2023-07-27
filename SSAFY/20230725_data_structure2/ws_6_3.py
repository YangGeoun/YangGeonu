# ws_6_3.py

# 아래 함수를 수정하시오.
# def intersection_sets(set_a, set_b):
#     return set_a.intersection(set_b)

def intersection_sets(set_a, set_b):
    temp_set = set()
    for el in set_a:
        if el in set_b:
            temp_set.add(el)
    return temp_set

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result) # {3}
