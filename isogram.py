def is_isogram(string):

    str_lst = list(string.lower())

    for char in str_lst:
        if char == '-' or char == ' ':
            str_lst.remove(char)

    return sorted(set(str_lst)) == sorted(str_lst)

print(is_isogram(""))