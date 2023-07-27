# ws_6_2.py

# 아래 함수를 수정하시오.
# def get_value_from_dict(dict,key):
#     res = dict.get(key)
#     return res

def get_value_from_dict(dict,key):
    return dict[key]

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice
