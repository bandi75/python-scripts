
def get_tuple_val(val):
    return val[-1]


list1 = [(1, 3), (3, 2), (2, 1)]
list2 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

list1.sort(key=get_tuple_val)
list2.sort(key=get_tuple_val)

print(list1)
print(list2)
