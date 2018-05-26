
def reduce_list(my_list):
    # Creating a new list
    new_list = [my_list[0]]
    j = 0
    for i in range(1, len(my_list)):
        if new_list[j] == my_list[i]:
            continue
        else:
            new_list.append(my_list[i])
            j = j+1

    return new_list


def reduce_list_new(my_list):
    # Modifying the same list
    val = my_list[0]
    pos = 1
    for n in my_list[1:]:
        if val == n:
            del my_list[pos]
        else:
            val = my_list[pos]
            pos = pos + 1

    return my_list


print(reduce_list([1, 2, 2, 3]))
print(reduce_list([2, 2, 3, 3, 3]))

print(reduce_list_new([1, 2, 2, 3]))
print(reduce_list_new([2, 2, 3, 3, 3]))
