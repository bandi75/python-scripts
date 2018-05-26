
def my_list_sort(my_list):
    x_list = []
    r_list = []
    for i in range(len(my_list)):
        if my_list[i][0] == 'x':
            x_list.append(my_list[i])
        else:
            r_list.append(my_list[i])

    r_list.sort()
    x_list.sort()

    return x_list + r_list


print(my_list_sort(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(my_list_sort(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))


