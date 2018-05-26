
def string_count(str_list):
    count = 0;
    for s in str_list:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1

    return count


print(string_count(['axa', 'xyz', 'gg', 'x', 'yyy']))
print(string_count(['x', 'cd', 'cnc', 'kk']))
print(string_count(['bab', 'ce', 'cba', 'syanora']))
