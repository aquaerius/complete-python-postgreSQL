l = lambda x: x*5

print(l(':D'))


def alter(values, check):
    return [val for val in values if check(val)]


my_list = [x for x in range(5)]
another_list = alter(my_list, lambda x: x != 3)
print(another_list)


def alter_with_filter(values, check):
    return list(filter(check, values))


another_list = alter_with_filter(my_list, lambda x: x != 3)
print(another_list)

# Filter method is pretty cool! use it filter out characters, etc


def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

